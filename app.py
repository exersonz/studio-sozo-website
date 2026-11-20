import os
from flask import Flask, render_template

app = Flask(__name__)

COMMISSION_FORM_URL = "https://docs.google.com/forms/d/1bYs78Cqnlo5k7U38rH_MGoZZxYja5dneQ4D7BNjPIMs/viewform"
VOLUNTEER_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf_tyEvDfEuydYH_9z5Dsof82SRR8Ev2TCQUYJtFFAQnNZ6Pg/viewform?fbclid=PAZXh0bgNhZW0CMTEAcGRvZgJzcnRjBmFwcF9pZA85MzY2MTk3NDMzOTI0NTkAAacruamPnU5d8Vfo-uSplcZHBD5fR_U_jXDT8yfdup420ZSRvOx3ned6tmiAAw_aem_QvaAjQD1ftUhzJ6IR9hIQg"
INSTAGRAM_HANDLE = "studiosozo_mv"
CONTACT_EMAIL = "studiosozo.mv@gmail.com"

WORKS_DIR = os.path.join(app.static_folder, "images", "works")
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".gif")

def get_works():
    """Every image dropped into static/images/works/ becomes a slide."""
    if not os.path.isdir(WORKS_DIR):
        return []
    files = sorted(f for f in os.listdir(WORKS_DIR) if f.lower().endswith(IMAGE_EXTS))
    return [f"images/works/{f}" for f in files]


@app.context_processor
def site_info():
    return dict(
        instagram=INSTAGRAM_HANDLE,
        email=CONTACT_EMAIL,
        commission_url=COMMISSION_FORM_URL,
        volunteer_url=VOLUNTEER_FORM_URL,
    )


@app.route("/")
def index():
    return render_template("index.html", works=get_works())


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
