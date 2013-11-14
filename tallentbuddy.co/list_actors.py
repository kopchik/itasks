#!/usr/bin/env python3


data = [ "Kevin Bacon, Tom Hanks, Gary Sinise, Ed Harris, Bill Paxton, Tom Cruise, Jack Nicholson, Demi Moore, Kiefer Sutherland",
"Tom Cruise, Nicole Kidman, Dustin Hoffman, Val Kilmer, Meg Ryan, Billy Connolly, Ken Watanabe, Renée Zellweger, Cuba Gooding Jr.",
"Nicole Kidman, Hugh Jackman, Ed Harris, Meryl Streep, Jeff Daniels, Toni Collette, Val Kilmer, Tommy Lee Jones, Jim Carrey",
"Tom Hanks, Meg Ryan, Tim Allen, Michael Keaton, Jean Reno, Vin Diesel, Matt Damon, Ted Danson, Ted Danson, Sally Field, Denzel Washington",
"Jeff Goldblum, Kevin Kline, William Hurt, Meg Tilly, Glenn Close, Tom Berenger, Bill Pullman, Will Smith, Vivica A. Fox, Brent Spiner",
"Jack Nicholson, Michael Keaton, Kim Basinger, Helen Hunt, Cuba Gooding Jr., Diane Keaton, Keanu Reeves, Marisa Tomei, Adam Sandler",
"Demi Moore, Patrick Swayze, Billy Bob Thornton, Billy Connolly, Woody Harrelson, Burt Reynolds, Jason Alexander, Jim Cummings",
"Brent Spiner, Patrick Stewart, Jonathan Frakes, LeVar Burton, Michael Dorn, Gates McFadden, Marina Sirtis, James Cromwell",
"Kiefer Sutherland, Charlie Sheen, Chris O'Donnell, Tim Curry, Sandra Bullock, Matthew McConaughey, Samuel L. Jackson, Julia Roberts",
"Dustin Hoffman, Robin Williams, Julia Roberts, Sharon Stone, Samuel L. Jackson, Liev Schreiber, Angelina Jolie, Jack Black, Jackie Chan",
"Meg Ryan, Billy Crystal, Carrie Fisher, Tim Robbins, Stephen Fry, Nicolas Cage, Sam Neill, Hugh Grant, Robert Downey Jr., Jean Reno",
"Sam Neill, Jeff Goldblum, Richard Attenborough, Samuel L. Jackson, Wayne Knight, Sean Connery, Alec Baldwin, James Earl Jones, Tim Curry"]

def list_actors(data, n):
  actors = {}
  for bucket in data:
    actor, *costars = bucket.split(", ")
    actors[actor] = costars

  def find(actors, actor="Kevin Bacon", n=n):
    if actor not in actors: return []
    if n==1: return actors[actor]
    r = []
    for a in actors[actor]:
      r += find(actors, a, n-1)
    return r
  print("\n".join(sorted(set(find(actors)))))


if __name__ == '__main__':
  list_actors(data, 5)
  
