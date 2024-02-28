DROP TABLE IF EXISTS Feedback;

CREATE TABLE Feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback_text TEXT NOT NULL,
    sentiment_result TEXT DEFAULT ''
);
