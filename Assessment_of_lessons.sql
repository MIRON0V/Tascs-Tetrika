SELECT date(scheduled_time) AS ride_date, user_id, ROUND((SUM(grade)/COUNT(user_id)),2) AS average_score

FROM  (SELECT user_id, role, event_id
       FROM test_db.users INNER JOIN  test_db.participants
       ON users.id = participants.user_id
       WHERE role = "tutor"
       GROUP BY event_id) event_participants
       INNER JOIN lessons
       ON lessons.event_id = event_participants.event_id 
       INNER JOIN 
      (SELECT lesson_id, (tech_quality / COUNT(lesson_id)) AS grade 
       FROM test_db.quality 
       WHERE tech_quality != 0 
       GROUP BY  lesson_id) grades
       ON lessons.id = grades.lesson_id 

WHERE subject = 'phys'
GROUP BY ride_date, user_id

ORDER BY ride_date, average_score
