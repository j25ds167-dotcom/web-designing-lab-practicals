# Experiment 9 - User Authentication

1. `npm install`
2. Copy `.env.example` to `.env` and fill in your own values.
   Generate a secret with:
   `node -e "console.log(require('crypto').randomBytes(48).toString('hex'))"`
3. Start MongoDB, then run `npm start` and open http://localhost:3000

Never commit the `.env` file.
