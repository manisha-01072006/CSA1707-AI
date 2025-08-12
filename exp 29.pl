% Facts: planet(Name, DistanceFromSun_km, Diameter_km, Moons)

planet(mercury, 57900000, 4879, 0).
planet(venus, 108200000, 12104, 0).
planet(earth, 149600000, 12742, 1).
planet(mars, 227900000, 6779, 2).
planet(jupiter, 778500000, 139820, 79).
planet(saturn, 1434000000, 116460, 82).
planet(uranus, 2871000000, 50724, 27).
planet(neptune, 4495000000, 49244, 14).

% Rules
has_moons(Planet) :-
    planet(Planet, _, _, Moons),
    Moons > 0.

is_closer_than(Planet1, Planet2) :-
    planet(Planet1, Dist1, _, _),
    planet(Planet2, Dist2, _, _),
    Dist1 < Dist2.

% Example Queries:
% 1. Find all planets
%    ?- planet(Name, _, _, _).
%
% 2. Planets with moons
%    ?- has_moons(P).
%
% 3. Planets closer to sun than Earth
%    ?- is_closer_than(P, earth).
