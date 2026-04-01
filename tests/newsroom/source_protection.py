# ruleid: manicode.newsroom.source-article-table-join-python
cursor.execute("SELECT * FROM source JOIN article ON source.story_id = article.id")

# ruleid: manicode.newsroom.analytics-in-tip-handler-python
@app.route("/securedrop/tip")
def submit_tip():
    analytics.track("tip-submitted")

# ok: manicode.newsroom.analytics-in-tip-handler-python
@app.route("/status")
def status():
    analytics.track("healthcheck")

