import glob
from os.path import splitext, basename
from os import walk
import sys
import imp
import inspect
from submission import Submission
import datetime

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
        submissions.append(submission)
    return submissions

def get_inputs_for_contest(contest_path):
    inputs = []
    # TODO : check if contest_path/inputs exists
    for input_file in glob.glob(contest_path + '/inputs/*.txt'):
        with open(input_file, 'r') as content_file:
            inputs.append((input_file.split('.')[-2].split('/')[-1],content_file.read()))
    return inputs

def _run_submission(submission_class, input):
    submission = submission_class()
    return submission.run(input), submission.author()

def run_submissions_for_contest(contest_path):
    print(bcolors.BOLD + "\t* contest %s:" % basename(contest_path) + bcolors.ENDC)
    submissions = load_submissions_for_contest(contest_path)
    inputs = get_inputs_for_contest(contest_path)

    try:
        for in_author, input in inputs:
            prev_ans = None
            for submission in submissions:
                time_before = datetime.datetime.now()
                answer, author = _run_submission(submission, input)
                time_after = datetime.datetime.now()
                msecs = (time_after - time_before).total_seconds() * 1000
                print("\t\t {green}{author}{end} says the response is {blue}{answer}{end} on input from {yellow}{input}{end} in {msecs} ms"
                .format(green=bcolors.GREEN, author=author, end=bcolors.ENDC, blue=bcolors.BLUE, answer=answer, input=in_author.title(), yellow=bcolors.YELLOW, msecs=msecs)
                )


                if prev_ans != None and prev_ans != answer:
                    raise DifferentAnswersException("\t\twe don't agree for %s" % contest_path)

                prev_ans = answer
    except DifferentAnswersException as e:
        print e
        sys.exit(1)


def run_submissions_for_day(day, day_path):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(bcolors.RED + bcolors.BOLD + "running submissions for day %s:" % day +bcolors.ENDC)

    contest_paths = _get_contests_path_for_day(day_path)
    for contest_path in contest_paths:
        run_submissions_for_contest(contest_path)

    print("\n")

def run_submissions():
    for day_path in _get_days():
        day = day_path[4:]
        run_submissions_for_day(day, day_path)













print(run_submissions())
