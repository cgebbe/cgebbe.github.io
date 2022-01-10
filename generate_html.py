from typing import Dict, List

HEADER = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Christian Gebbe">
    <link rel="icon" href="https://getbootstrap.com/docs/4.0/assets/img/favicons/favicon.ico">

    <title>cgebbe.github.io</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/album/">

    <!-- Bootstrap core CSS -->
    <link href="bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="album.css" rel="stylesheet">
  </head>

  <body>
    <main role="main">

      <section class="jumbotron text-center" style="background: #404040;">
        <div class="container">
          <h1 class="jumbotron-heading" style="color: #fff;">cgebbe.github.io</h1>
          <p class="lead text-muted" style="color: #f00;">repository overview</p>
        </div>
      </section>
"""
FOOTER = """
    </main>

  </body>
</html>
"""

SECTION_BEGIN = """
    <h3 style="text-align: center;">{heading}</h3>
      <div class="album py-5 bg-light">
        <div class="container">
          <div class="row">
"""
SECTION_END = """
          </div>
        </div>
      </div>
"""
ITEM_TEMPLATE = """
            <div class="col-md-4">
            <a href="{link}">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" src="{image_path}" alt="{description}"  style="object-fit: contain; max-height: 200px;">
                <div class="card-body">
                  <p class="card-text">{description}</p>
                </div>
              </div>
            </a>
            </div>
"""


class Item:
    def __init__(self, image_path: str, description: str, link: str) -> None:
        self.image_path = image_path
        self.description = description
        self.link = link

    def to_html(self) -> str:
        return ITEM_TEMPLATE.format(
            image_path=self.image_path,
            description=self.description,
            link=self.link,
        )


def _create_html(items_by_section: Dict[str, List[Item]]) -> str:
    page = ""
    page += HEADER
    for section, items in items_by_section.items():
        page += SECTION_BEGIN.format(heading=section)
        for item in items:
            page += item.to_html()
        page += SECTION_END
    return page


def _get_items_by_section() -> Dict[str, List[Item]]:
    items_by_section = dict()
    items_by_section["Courses"] = [
        Item(
            image_path="imgs/courses/udacity_carnd.gif",
            description="Udacity Nanodegree Self-Driving Car Engineer",
            link="https://cgebbe.github.io/udacity_nanodegree_selfdriving",
        ),
        Item(
            image_path="imgs/courses/coursera_perception.gif",
            description="Coursera course Robotics: perception",
            link="https://github.com/cgebbe/coursera_robotics_perception",
        ),
        Item(
            image_path="imgs/courses/kaggle.png",
            description="Coursera course: How to win a data science competition",
            link="https://github.com/cgebbe/coursera_win_competition",
        ),
        Item(
            image_path="imgs/courses/full_stack_deep_learning.png",
            description="Online course: Full Stack Deep Learning",
            link="https://github.com/cgebbe/course_full_stack_deep_learning",
        ),
    ]
    items_by_section["Competitions"] = [
        Item(
            image_path="imgs/competitions/kaggle_3dcar.png",
            description="Kaggle: 3D car detection",
            link="https://github.com/cgebbe/kaggle_pku-autonomous-driving",
        ),
        Item(
            image_path="imgs/competitions/kaggle_future_sales.png",
            description="Kaggle: Predict future sales",
            link="https://github.com/cgebbe/kaggle_predict_future_sales",
        ),
        Item(
            image_path="imgs/competitions/leetcode.png",
            description="Leetcode: Solved 143 data structures and algorithms puzzles",
            link="https://leetcode.com/cgebbe/",
        ),
        Item(
            image_path="imgs/competitions/kaggle_ventilator_pressure.png",
            description="Kaggle: ventilator pressure prediction",
            link="https://github.com/cgebbe/kaggle_ventilator_pressure",
        ),
    ]
    items_by_section["Prototpyes"] = [
        Item(
            image_path="imgs/demos/ner_nobel_laureate.png",
            description="Named-entity recognition (NER) using huggingface",
            link="https://github.com/cgebbe/prototype_ner_nobel_laureate",
        ),
        Item(
            image_path="imgs/demos/slam.gif",
            description="Simple SLAM pipeline using opencv",
            link="https://github.com/cgebbe/demo_slam",
        ),
        Item(
            image_path="imgs/demos/adam_optimizer.png",
            description="Understanding Adam (the optimization algorithm)",
            link="https://github.com/cgebbe/demo_optimizer",
        ),
        Item(
            image_path="imgs/demos/style_transfer_gatys.png",
            description="Style transfer according to Gatys et al.",
            link="https://github.com/cgebbe/demo_style_gatys",
        ),
        Item(
            image_path="imgs/demos/kalman.png",
            description="Understanding Bayes, Kalman and Particle filter",
            link="https://github.com/cgebbe/demo_kalman",
        ),
        Item(
            image_path="imgs/demos/job_skills.png",
            description="Clustering job postings using BERT embeddings",
            link="https://cgebbe.medium.com/clustering-job-postings-by-skills-b33e0ad579ff",
        ),
    ]
    return items_by_section


if __name__ == "__main__":
    items_by_section = _get_items_by_section()
    page = _create_html(items_by_section)
    with open("index.html", "w") as f:
        f.write(page)
