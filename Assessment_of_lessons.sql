SELECT date(scheduled_time) AS ride_date, user_id, ROUND((SUM(grade)/COUNT(user_id)),2) AS average_score                              
FROM (SELECT id FROM test_db.users WHERE role = "pupil") query_in_1
      INNER JOIN 
     (SELECT user_id, event_id FROM test_db.participants GROUP BY user_id) query_in_2
      ON query_in_2.user_id = query_in_1.id 
      INNER JOIN 
      test_db.lessons 
      ON lessons.event_id = query_in_2.event_id
      INNER JOIN 
     (SELECT lesson_id, (tech_quality / COUNT(lesson_id)) AS grade FROM test_db.quality WHERE tech_quality != 0 GROUP BY  lesson_id) grades
      ON lessons.id = grades.lesson_id 

WHERE subject = "phys"
GROUP BY ride_date
ORDER BY ride_date, user_id DESC


