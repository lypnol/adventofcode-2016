# python libs
import glob, sys, getopt, imp, inspect, datetime, re
from os.path import splitext, basename
from os import walk

from submission import Submission

show_debug = False
filter_author = None

#To print colors in terminal
class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


DAY_PATH_PATTERN  = 'day-[0-9]*'
CONTEST_PATH_PATTERN = 'part-[0-9]*'

class DifferentAnswersException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def _context_name(context_path):
    return context_path.replace('/','_').replace('-','_')

# Return the list of the contests
# It should be the list of the directories matching day-<a number>
def _get_days():
    return glob.glob(DAY_PATH_PATTERN)

# Return the list of the contests path for the given day path
def _get_contests_path_for_day(day_path):
    return glob.glob(day_path + '/' + CONTEST_PATH_PATTERN)

# Return contest number from path
def _get_constest_number(contest_path):
    return contest_path.split('-')[-1]

# Returns the lists of possible submission files for the given contest
def _find_submissions_for_contest(contest_path):
    submission_files = []
    for _, _, files in walk(contest_path):
        for filename in files:
            submission, ext = splitext(filename)
            if ext == '.py':
                submission_files.append(submission)
    return submission_files

def _load_submission(contest_path, submission):
    submission_path = '%s/%s.py' % (contest_path, submission)
    contest = _context_name(contest_path)
    submission_module = imp.load_source('submission_%s_%s' % (contest, submission), submission_path)

    submission_class = None
    classes = inspect.getmembers(submission_module, inspect.isclass)
    for _, cls_submission in classes:
        if issubclass(cls_submission, Submission):
            return cls_submission

    return None

def load_submissions_for_contest(contest_path):
    submission_files = _find_submissions_for_contest(contest_path)
    contest = _context_name(contest_path)
    submissions = []
    for submission_file in submission_files:
        submission = _load_submission(contest_path, submission_file)

        # TODO : check if submission is None
        if submission is not None:
            submissions.append(submission)
    return submissions

def get_inputs_for_contest(contest_path):
    inputs = []
    # TODO : check if contest_path/inputs exists
    for input_file in glob.glob(contest_path + '/inputs/*.txt'):
        with open(input_file, 'r') as content_file:
            inputs.append((input_file.split('.')[-2].split('/')[-1],content_file.read()))
    return inputs

def _run_submission(submission, input):
    result, author = submission.run(input), submission.author()
    if show_debug:
        if len(submission.get_debug_stack()) > 0:
            print("Debug trace for %s " % author)
            stack = submission.get_debug_stack()
            print('\n'.join(submission.get_debug_stack()[:15]))
            if len(stack) > 15:
                print('and %s other lines...' % (len(stack) - 15))
    return result, author

def run_submissions_for_contest(contest_path):
    print("\n\t" + bcolors.MAGENTA + bcolors.BOLD + "* contest %s:" % basename(contest_path) + bcolors.ENDC)
    submissions = load_submissions_for_contest(contest_path)
    inputs = get_inputs_for_contest(contest_path)

    try:
        for in_author, input in inputs:
            prev_ans = None
            answers = []
            print("\t---------------------------------------------------")
            print("\tOn input from {yellow}{input}{end}".format(
                yellow=bcolors.YELLOW,
                end=bcolors.ENDC,
                input=in_author.title()))
            print("\t---------------------------------------------------")
            for submission in submissions:
                time_before = datetime.datetime.now()
                submission_obj = submission()
                if filter_author is not None and submission_obj.author().lower() != filter_author.lower():
                    continue
                answer, author = _run_submission(submission_obj, input)
                time_after = datetime.datetime.now()
                msecs = (time_after - time_before).total_seconds() * 1000
                print("\t\t{green}{author}{end}\t | {blue}{answer}{end} \t | {msecs} ms".format(
                    green=bcolors.GREEN,
                    author=author.title(),
                    end=bcolors.ENDC,
                    blue=bcolors.BLUE,
                    answer=answer,
                    input=in_author.title(),
                    yellow=bcolors.YELLOW,
                    msecs=msecs))

                if prev_ans != None and prev_ans != str(answer):
                    raise DifferentAnswersException("\t\twe don't agree for %s" % contest_path)

                prev_ans = str(answer)
    except DifferentAnswersException as e:
        print e
        sys.exit(1)


def run_submissions_for_day(day, day_path, contestFilter=None):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(bcolors.RED + bcolors.BOLD + "Running submissions for day %s:" % day +bcolors.ENDC)

    contest_paths = _get_contests_path_for_day(day_path)
    for contest_path in contest_paths:
        if contestFilter != None and _get_constest_number(contest_path) == contestFilter:
            run_submissions_for_contest(contest_path)
        elif contestFilter == None:
            run_submissions_for_contest(contest_path)

    print("\n")

def run_submissions():
    for day_path in _get_days():
        day = day_path[4:]
        run_submissions_for_day(day, day_path)


def main(argv):
    global show_debug
    global filter_author
    day = None
    part = None
    smartDetection = False
    try:
        opts, args = getopt.getopt(argv,"hd:p:",["day=","part=", "debug", "no-debug", "author=", 'last'])
    except getopt.GetoptError:
        print 'main.py -d <day-number> -p <contest-number>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'main.py -d <day-number> -p <contest-number>'
            sys.exit()
        elif opt in ("-d", "--day"):
            day = arg
        elif opt in ("-p", "--part"):
            part = arg
        elif opt == '--last':
            day = _get_days()[-1][4:]
        elif opt == '--debug':
            show_debug = True
        elif opt == '--no-debug':
            show_debug = False
        elif opt in ["-a", "--author"]:
            filter_author = arg

    if not (part is None) and day is None:
        for day_path in _get_days():
            day = day_path[4:]
            run_submissions_for_day(day, day_path, part)
        return

    if day == None and part == None:
        # Full test
        run_submissions()
        return

    if part == None:
        run_submissions_for_day(day, 'day-%s' % day)
        return

    run_submissions_for_day(day,'day-%s' % day, part)
    return

if __name__ == "__main__":
   main(sys.argv[1:])
