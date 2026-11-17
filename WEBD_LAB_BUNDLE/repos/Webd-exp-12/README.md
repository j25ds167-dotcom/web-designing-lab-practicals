# Experiment 12 - MERN Task Manager

Backend: `cd backend && npm install`, copy `.env.example` to `.env`, `npm start`.
Frontend: `cd frontend && npm install && npm run dev`.

Deployment: host `backend/` as a Node web service (set MONGO_URI as an
environment variable) and `frontend/` as a static site (build command
`npm run build`, publish directory `dist`, set VITE_API_URL to the backend URL).
