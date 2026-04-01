const resolver = async (parent, args, ctx) => {
  // ruleid: manicode.graphql.resolver-sql-injection
  db.query(`select * from users where id = ${args.userId}`);
};

const safeResolver = async (parent, args, ctx) => {
  // ok: manicode.graphql.resolver-sql-injection
  db.query("select * from users where id = ?", [args.userId]);
};
