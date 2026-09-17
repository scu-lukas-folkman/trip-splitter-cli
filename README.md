# trip-splitter

Work out who owes what after a trip away. A deliberately small Python module,
used in **ISYS3001 Module 03** to learn Git, GitHub and the way a team works on
one codebase at the same time. X.

## Running the tests

```bash
python -m pip install -r requirements.txt
python -m pytest
```

Five tests. They should all pass the moment you clone this — if they do not,
fix that before anything else, because everything later in the lecture assumes
a green start.

## The sprint

Our board lives in Jira, in project **TRIP**. Sprint 1:

| Key | Item | Status |
|---|---|---|
| TRIP-2 | Split a trip's expenses evenly between people | Done |
| TRIP-3 | Show amounts as dollars and cents | Done |
| TRIP-4 | Show the largest single expense | **Yours** |
| TRIP-5 | Show the smallest single expense | A teammate |
| TRIP-6 | Round each share up so the group is never short | A teammate |
| TRIP-7 | Use clearer function names in `splitter.py` | A teammate |
| TRIP-9 | Show a summary line for the whole trip | **Yours** |

Every story has acceptance criteria on the board. Read them before you start —
they are what tells you when you are finished.

## How we work

One branch per story, named after its key:

```
feature/TRIP-4-largest
```

Small commits, each message starting with the key:

```
TRIP-4 Add largest() for the biggest single expense
```

Then a pull request, a review, and a merge. `main` always works.

## Contributors

- Add your name here in your first commit.
