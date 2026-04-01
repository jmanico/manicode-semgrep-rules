// ruleid: manicode.newsroom.draft-endpoint-no-auth-express
app.get("/preview/story", (req, res) => {
  res.json({ draft: true });
});

// ruleid: manicode.newsroom.admin-route-no-mfa-js
app.get("/cms/manage/users", (req, res) => {
  res.send("ok");
});

// ok: manicode.newsroom.admin-route-no-mfa-js
app.get("/cms/manage/users", mfaRequired, (req, res) => {
  res.send("ok");
});

