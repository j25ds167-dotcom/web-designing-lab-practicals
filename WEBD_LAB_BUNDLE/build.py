import os, shutil, textwrap, sys
sys.path.insert(0, os.path.dirname(__file__))
from content1 import *
from content2 import *
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "repos")
EXPS = [EXP1, EXP2, EXP3, EXP4, EXP5, EXP6, EXP7, EXP8, EXP9, EXP10, EXP11, EXP12]

FACULTY = "MR. GANESH KUMAR YADAV"
SUBJECT = "JCS 308/408"


def gradient(path, c1, c2, size=(600, 400), fmt=None):
    img = Image.new("RGB", size)
    d = ImageDraw.Draw(img)
    for y in range(size[1]):
        t = y / (size[1] - 1)
        col = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        d.line([(0, y), (size[0], y)], fill=col)
    img.save(path, fmt)


def write_repos():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    for e in EXPS:
        base = os.path.join(OUT, "Webd-exp-%d" % e["n"])
        for rel, content in e["files"]:
            p = os.path.join(base, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(content)
    # generated images
    gradient(os.path.join(OUT, "Webd-exp-4", "web-design.jpg"), (30, 60, 120), (120, 190, 255), (500, 330))
    gradient(os.path.join(OUT, "Webd-exp-11", "photo1.jpg"), (255, 140, 60), (255, 220, 120), (600, 400))
    gradient(os.path.join(OUT, "Webd-exp-11", "photo2.jpg"), (20, 90, 160), (120, 220, 230), (600, 400))
    gradient(os.path.join(OUT, "Webd-exp-11", "photo3.jpg"), (20, 90, 50), (150, 210, 110), (600, 400))


# ---------------- push script ----------------
PUSH = r'''#!/usr/bin/env bash
# Creates the 12 repositories on GitHub under %(user)s, pushes the code,
# and turns on GitHub Pages where it applies.
#
# Before running:   gh auth login      (log in once, in your own terminal)
# Run from the folder that contains the "repos" folder:   bash push.sh
set -e

USER_NAME="%(user)s"
GIT_NAME="%(name)s"
GIT_EMAIL="%(email)s"
HERE="$(cd "$(dirname "$0")" && pwd)"

gh auth status >/dev/null 2>&1 || { echo "Please run 'gh auth login' first."; exit 1; }

# Pages: "root" = publish main branch root, "docs" = publish main /docs, "none" = no Pages
declare -A PAGES=( [1]=root [2]=root [3]=root [4]=root [5]=root [6]=root [7]=docs [8]=none [9]=none [10]=root [11]=root [12]=none )

enable_pages () {
  local repo="$1" path="$2"
  gh api -X POST "repos/$USER_NAME/$repo/pages" -f "source[branch]=main" -f "source[path]=$path" >/dev/null 2>&1 \
    || gh api -X PUT "repos/$USER_NAME/$repo/pages" -f "source[branch]=main" -f "source[path]=$path" >/dev/null 2>&1 \
    || echo "  (could not enable Pages automatically - enable it in repo Settings > Pages)"
}

for n in $(seq 1 12); do
  REPO="Webd-exp-$n"
  DIR="$HERE/repos/$REPO"
  echo "=== $REPO ==="
  cd "$DIR"

  rm -rf .git
  git init -q -b main
  git config user.name "$GIT_NAME"
  git config user.email "$GIT_EMAIL"

  # Experiment 7 is a Vite app: build it and publish the build output from /docs
  if [ "$n" = "7" ]; then
    npm install --silent && npm run build --silent
    rm -rf docs && cp -r dist docs
  fi

  git add -A
  git commit -q -m "Initial commit: experiment $n"

  # Experiment 1: practise branching and merging
  if [ "$n" = "1" ]; then
    git checkout -q -b feature-update
    sed -i 's#<p>This is my first hosted website.</p>#<p>This is my first hosted website, updated on a feature branch.</p>#' index.html
    git commit -q -am "Update welcome text on feature branch"
    git checkout -q main
    git merge -q --no-ff feature-update -m "Merge feature-update into main"
  fi

  if ! gh repo view "$USER_NAME/$REPO" >/dev/null 2>&1; then
    gh repo create "$USER_NAME/$REPO" --public --description "Web Designing Lab - Experiment $n" >/dev/null
  fi
  git remote remove origin 2>/dev/null || true
  git remote add origin "https://github.com/$USER_NAME/$REPO.git"
  git push -q -u origin main --force
  [ "$n" = "1" ] && git push -q origin feature-update --force

  case "${PAGES[$n]}" in
    root) enable_pages "$REPO" "/" ;;
    docs) enable_pages "$REPO" "/docs" ;;
  esac
  echo "  repo: https://github.com/$USER_NAME/$REPO"
  [ "${PAGES[$n]}" != "none" ] && echo "  site: https://$USER_NAME.github.io/$REPO/  (takes 1-2 minutes to go live)"
done
echo "Done."
''' % dict(user=GH_USER, name=NAME, email=EMAIL)


def write_push():
    p = os.path.join(ROOT, "push.sh")
    with open(p, "w", newline="\n") as f:
        f.write(PUSH)
    os.chmod(p, 0o755)


if __name__ == "__main__":
    write_repos()
    write_push()
    print("repos + push.sh written")
