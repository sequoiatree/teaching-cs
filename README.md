# UC Berkeley's CS 370: Introduction to Teaching Computer Science

The official repository for UC Berkeley's CS 370: Introduction to Teaching Computer Science.

## Viewing the staff timeline

During the semester, staff can view their weekly tasks at [http://inst.eecs.berkeley.edu/~cs370/fa18/timeline.html](http://inst.eecs.berkeley.edu/~cs370/fa18/timeline.html), where "fa18" is replaced by the appropriate semester code.

## Setting up

To contribute to this repository, first clone it as you would any `git` repository. Then set up a virtual environment and install the requirements.

```bash
git clone https://github.com/sequoia-tree/cs-370.git
cd cs-370
virtualenv -p python3 webenv
pip install -r requirements.txt
```

If you tend to make a lot of virtual environments, I recommend aliasing a `mkenv` command to speed up the process. Here's how to do it on a Mac:

```bash
cd ~
open .bash_profile
```

Then add the line `mkenv() { virtualenv -p python3 $1; }`. In the future, you'll be able to set up your virtual environment for this project by simply executing `mkenv webenv`.

## Making edits

After you're all set up, you can make changes to your local clone of the repository.

### Transitioning between semesters

Semester metadata is catalogued in `src/semester.py`. In particular you need to update the dictionary `META` to enable automatic content generation. Should you want to, you can also change `TIME_UNTIL_RELEASED` to modify assignment release dates. Finally, to change the point at which we'll cover topics in the class, you should alter `CURRICULUM_WITH_SIGNUPS`. Speaking of which, the sign-up links should also be refreshed on a per-semester basis.

### Updating static files

Should you need to update static files, such as the course policies page, then navigate to the `src/static/md` directory. Meanwhile, staff information can be found in `src/staff` and staff photos should be curated in `src/static/img`.

### Writing resources

Resources include readings, homework, tutoring assignments / prompts, announcements, etc. You may specify in `models.py` the files which should be stitched together to create these resources, and the templates they draw from. From there you can also configure which resources display automatically `index.html`.

All resources are organized both topically and weekly. Each week in fact refers to several composite assignments, stitched together in `models.py` from the relevant topical and weekly assignments found under the `src/curriculum` directory. In the interest of efficiency HTML will only be generated if the old HTML is first deleted from `composite-resources`. You can also safely remove the entirety of the `composite-resources` directory, should you want to build the entire website from scratch.

### Validating edits

If you want to see how your changes affect the website, navigate to the `src` directory from within your terminal and execute `python3 run.py`. Then, using a web browser, go to the URL `localhost:5000/`.

## Deploying edits

To make sure your changes are actually reflected on [http://inst.eecs.berkeley.edu/~cs370](http://inst.eecs.berkeley.edu/~cs370/), you need to freeze the dynamic Flask app. From within `src`, run `python3 freeze.py`. This will build the entire website's static content in `src/build`. Then you can commit and push your changes to Github.