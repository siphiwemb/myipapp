var user = {
    user: "siphiwe",
    pwd: "jrvmgYTUSL6756HGJHopxa",
    roles: [
        {
            role: "root",
            db: "admin"
        }
    ],
    mechanisms:[  
        "SCRAM-SHA-1"
    ]
};

if (!db.getUser(user.user)) {
    db.createUser(user);
}
