import movie
import fresh_tomatoes
# Different instance of Movies class
avatar = movie.Movies('Avatar',
                      'A marine on an alien planet',
                      'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                      'https://www.youtube.com/watch?v=-9ceBgWV8io')
school_of_rock = movie.Movies('School Of Rock',
                      'Using rock Music to learn',
                      'http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                      'https://www.youtube.com/watch?v=3PsUJFEBC74')
toy_story = movie.Movies('Toy Story 2',
                      'Story of a toy Woody',
                      'https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg',
                      'https://www.youtube.com/watch?v=Lu0sotERXhI')
jurrasic_world = movie.Movies('Jurrasic World',
                      'Theme Park of Dinosaurs',
                      'https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg',
                      'https://www.youtube.com/watch?v=RFinNxS5KN4')
# List of Movies
movies = [avatar, school_of_rock, toy_story, jurrasic_world]
# Open movies page
fresh_tomatoes.open_movies_page(movies)
# Print the information about Movies class documentation.
print(movie.Movies.__doc__)
