import pytest
from battleships import *


def test_is_sunk1():
    s = (2, 3, False, 3, {(2, 3), (3, 3), (4, 3)})
    assert is_sunk(s) == True
    # add tests for each ship size and horizontal/vertical including outer edge
    # submarine - would not enter unless = sunk is true


def test_is_sunk2():
    s = (3, 3, False, 1, {(3, 3)})  # submarine vertical
    assert is_sunk(s) == True


def test_is_sunk3():
    s = (0, 0, True, 1, {(0, 0)})  # submarine horizontal
    assert is_sunk(s) == True


def test_is_sunk4():
    # destroyer true
    s = (3, 3, False, 2, {(3, 3), (4, 3)})  # destroyer vertical
    assert is_sunk(s) == True

def test_is_sunk5():
    s = (0, 0, True, 2, {(0, 0), (1, 0)})  # destroyer horizontal
    assert is_sunk(s) == True

def test_is_sunk6():
    # destroyer false
    s = (3, 3, False, 2, {(3, 3)})  # destroyer vertical
    assert is_sunk(s) == False

def test_is_sunk7():
    s = (0, 0, True, 2, {(0, 0)})  # destroyer horizontal
    assert is_sunk(s) == False

def test_is_sunk8():
    # cruiser true
    s = (3, 3, False, 3, {(3, 3), (4, 3), (5, 3)})  # cruiser vertical
    assert is_sunk(s) == True

def test_is_sunk9():
    s = (0, 0, True, 3, {(0, 0), (1, 0), (2, 0)})  # cruiser horizontal
    assert is_sunk(s) == True

def test_is_sunk10():
    # cruiser false
    s = (3, 3, False, 3, {(3, 3), (4, 3)})  # cruiser vertical
    assert is_sunk(s) == False

def test_is_sunk11():
    s = (0, 0, True, 3, {(0, 0), (0, 1)})  # cruiser horizontal
    assert is_sunk(s) == False

def test_is_sunk12():
    # battleship true
    s = (3, 3, False, 4, {(3, 3), (4, 3), (5, 3), (6, 3)})  # battleship vertical
    assert is_sunk(s) == True

def test_is_sunk13():
    s = (0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)})  # battleship horizontal
    assert is_sunk(s) == True

def test_is_sunk14():
    # battleship false
    s = (3, 3, False, 4, {(3, 3), (4, 3), (5, 3)})  # battleship vertical
    assert is_sunk(s) == False

def test_is_sunk15():
    s = (0, 0, True, 4, {(0, 0), (0, 1), (0, 2)})  # battleship horizontal
    assert is_sunk(s) == False


def test_ship_type1():
    # battleship
    s = (3, 3, False, 4, {(3, 3), (4, 3), (5, 3), (6, 3)})  # battleship vertical
    assert ship_type(s) == "battleship"


def test_ship_type2():
    s = (0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)})  # battleship horizontal
    assert ship_type(s) == "battleship"

def test_ship_type3():
    # cruiser
    s = (3, 3, False, 3, {(3, 3), (4, 3), (5, 3)})  # cruiser vertical
    assert ship_type(s) == "cruiser"

def test_ship_type4():
    s = (0, 0, True, 3, {(0, 0), (0, 1), (0, 2)})  # cruiser horizontal
    assert ship_type(s) == "cruiser"

def test_ship_type5():
    # destroyer
    s = (3, 3, False, 2, {(3, 3), (4, 3)})  # destroyer vertical
    assert ship_type(s) == "destroyer"

def test_ship_type6():
    s = (0, 0, True, 2, {(0, 0), (0, 1)})  # destroyer horizontal
    assert ship_type(s) == "destroyer"

def test_ship_type7():
    # submarine
    s = (3, 3, False, 1, {(3, 3)})  # submarine vertical
    assert ship_type(s) == "submarine"

def test_ship_type8():
    s = (0, 0, True, 1, {(0, 0)})  # submarine horizontal
    assert ship_type(s) == "submarine"


def test_is_open_sea1():
    # row,column,fleet -> Boolean
    # test whole ship false
    assert is_open_sea(2, 0, [(2, 0, True, 4, set())]) == False


def test_is_open_sea2():
    assert is_open_sea(2, 1, [(2, 0, True, 4, set())]) == False


def test_is_open_sea3():
    assert is_open_sea(2, 2, [(2, 0, True, 4, set())]) == False


def test_is_open_sea4():
    assert is_open_sea(2, 3, [(2, 0, True, 4, set())]) == False

    # test diagonal, horizontal, vertical, of ship


def test_is_open_sea5():
    # horizontal
    assert is_open_sea(2, 2, [(2, 3, True, 4, set())]) == False


def test_is_open_sea6():
    # vertical
    assert is_open_sea(2, 3, [(1, 2, True, 4, set())]) == False


def test_is_open_sea7():
    # diagonal
    assert is_open_sea(2, 3, [(1, 4, True, 4, set())]) == False


def test_is_open_sea8():
    # test random ship is true
    assert is_open_sea(9, 9, [(2, 3, True, 4, set())]) == True


fleet_missing_sub = [(0, 0, True, 4, set()),
                     (0, 5, True, 3, set()),
                     (2, 0, True, 3, set()),
                     (2, 4, True, 2, set()),
                     (2, 7, True, 2, set()),
                     (4, 0, True, 2, set()),
                     (4, 3, False, 1, set()),
                     (4, 5, True, 1, set()),
                     (4, 7, True, 1, set())]
ship1 = (2, 3, True, 4, set())
ship2 = (9, 9, False, 1, set())
fleet = [ship1, ship2]


def test_ok_to_place_ship_at1():  # input (row, column, horizontal, length, fleet) returns boolean
    fleet_missing_des = [(0, 0, True, 4, set()),
                         (0, 5, True, 3, set()),
                         (2, 0, True, 3, set()),
                         (2, 4, True, 2, set()),
                         (2, 7, True, 2, set())]

    assert ok_to_place_ship_at(4, 9, False, 1, fleet_missing_sub) == True
    # add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    # provide at least five tests in total for ok_to_place_ship_at by the project submission deadline


def test_ok_to_place_ship_at2():
    assert ok_to_place_ship_at(0, 3, False, 1, fleet_missing_sub) == False  # ship with coords already in fleet


def test_ok_to_place_ship_at3():
    assert ok_to_place_ship_at(0, 2, False, 1, fleet_missing_sub) == False  # ship with coords in fleet


def test_ok_to_place_ship_at4():
    assert ok_to_place_ship_at(5, 2, False, 1,
                               fleet_missing_sub) == False  # ship with coords diagonal to existing


def test_ok_to_place_ship_at5():
    assert ok_to_place_ship_at(5, 1, False, 1,
                               fleet_missing_sub) == False  # ship with coords horizontal to existing


def test_ok_to_place_ship_at6():
    assert ok_to_place_ship_at(4, 2, False, 1,
                               fleet_missing_sub) == False  # ship with coords vertical to existing


def test_ok_to_place_ship_at7():
    assert ok_to_place_ship_at(9, 9, True, 2,
                               fleet) == False  # ship with coordinates that won't fit map (<9) horizontal


def test_ok_to_place_ship_at8():
    assert ok_to_place_ship_at(9, 1, False, 2, fleet) == False  # ship with coordinates that won't fit map (>9) vertical


fleet_missing_sub = [(0, 0, True, 4, set()),
                     (0, 5, True, 3, set()),
                     (2, 0, True, 3, set()),
                     (2, 4, True, 2, set()),
                     (2, 7, True, 2, set()),
                     (4, 0, True, 2, set()),
                     (4, 3, False, 1, set()),
                     (4, 5, True, 1, set()),
                     (4, 7, True, 1, set())]
fleet_missing_des = [(0, 0, True, 4, set()),
                     (0, 5, True, 3, set()),
                     (2, 0, True, 3, set()),
                     (2, 4, True, 2, set()),
                     (2, 7, True, 2, set())]


def test_place_ship_at1():  # input (row, column, horizontal, length, fleet) returns fleet
    # add at least one test for place_ship_at by the deadline of session 7 assignment
    # provide at least five tests in total for place_ship_at by the project submission deadline

    # place last submarine
    actual = place_ship_at(4, 9, True, 1, fleet_missing_sub)  # place sub
    actual.sort()
    full_fleet.sort()
    assert actual == full_fleet


def test_place_ship_at2():
    actual = place_ship_at(0, 3, True, 4, [])  # place battleship
    actual.sort()
    assert actual == [(0, 3, True, 4, set())]


def test_place_ship_at3():
    actual = place_ship_at(2, 2, True, 3, [(0, 3, True, 4, set()), (0, 7, True, 3, set())])
    actual.sort()
    # place cruiser
    assert actual == [(0, 3, True, 4, set()), (0, 7, True, 3, set()), (2, 2, True, 3, set())]


def test_place_ship_at4():
    actual = place_ship_at(4, 1, True, 2, fleet_missing_des)  # place destroyer
    actual.sort()
    assert actual == [(0, 0, True, 4, set()),
                      (0, 5, True, 3, set()),
                      (2, 0, True, 3, set()),
                      (2, 4, True, 2, set()),
                      (2, 7, True, 2, set()),
                      (4, 1, True, 2, set())]


def test_place_ship_at5():
    actual = place_ship_at(4, 1, False, 2, [(0, 0, True, 4, set()),
                                            (0, 5, True, 3, set()),
                                            (2, 0, True, 3, set()),
                                            (2, 4, True, 2, set()), ])  # place vertical ship
    actual.sort()
    assert actual == [(0, 0, True, 4, set()),
                      (0, 5, True, 3, set()),
                      (2, 0, True, 3, set()),
                      (2, 4, True, 2, set()),
                      (4, 1, False, 2, set())]


full_fleet = [(0, 0, True, 4, set()),
              (0, 5, True, 3, set()),
              (2, 0, True, 3, set()),
              (2, 4, True, 2, set()),
              (2, 7, True, 2, set()),
              (4, 0, True, 2, set()),
              (4, 3, False, 1, set()),
              (4, 5, True, 1, set()),
              (4, 7, True, 1, set()),
              (4, 9, True, 1, set())]


def test_check_if_hits1():  # row,column,fleet -> Boolean
    # add at least one test for check_if_hits by the deadline of session 7 assignment
    # provide at least five tests in total for check_if_hits by the project submission deadline
    # hits val in fleet
    actual = check_if_hits(2, 0, full_fleet)
    assert actual == True


def test_check_if_hits2():
    # hits - val not recorded in fleet coordinates (needs to be deduced)
    actual = check_if_hits(2, 1, full_fleet)
    assert actual == True


def test_check_if_hits3():
    # misses square next to ship horizontally
    actual = check_if_hits(4, 2, full_fleet)
    assert actual == False


def test_check_if_hits4():
    # misses square next to ship vertically
    actual = check_if_hits(5, 1, full_fleet)
    assert actual == False


def test_check_if_hits5():
    # misses square next to ship diagonally
    actual = check_if_hits(5, 2, full_fleet)
    assert actual == False


def test_check_if_hits6():
    # misses in open ocean
    actual = check_if_hits(8, 2, full_fleet)
    assert actual == False


ship1 = (2, 3, True, 4, set())  # same as above, copied for clarity
ship2 = (9, 9, False, 1, set())
fleet = [ship1, ship2]


def test_hit1():  # input row column fleet -> output new fleet, new ship
    newfleet, ship = hit(2, 3, [(2, 3, True, 4, set()), (9, 9, False, 1, set())])  # first hit
    newfleet.sort()
    result = (newfleet, ship)
    assert result == ([(2, 3, True, 4, {(2, 3)}), (9, 9, False, 1, set())],
                      (2, 3, True, 4, {(2, 3)}))  # hit
    # add at least one test for hit by the deadline of session 7 assignment
    # provide at least five tests in total for hit by the project submission deadline


ship1 = (0, 0, True, 4, {(0, 3)})  # copied for clarity
ship2 = (9, 9, False, 1, set())
fleet = [ship1, ship2]


def test_hit2():
    newfleet, ship = hit(0, 2, fleet)  # double hit
    newfleet.sort()
    result = (newfleet, ship)
    assert result == ([(0, 0, True, 4, {(0, 2), (0, 3)}), (9, 9, False, 1, set())],
                      (0, 0, True, 4, {(0, 2), (0, 3)}))


def test_hit3():
    newfleet, ship = hit(0, 1, [(0, 0, True, 4, {(0, 2), (0, 3)}), (9, 9, False, 1, set())])  # triple hit
    newfleet.sort()
    result = (newfleet, ship)
    assert result == ([(0, 0, True, 4, {(0, 2), (0, 3), (0, 1)}),
                       (9, 9, False, 1, set())],
                      (0, 0, True, 4, {(0, 2), (0, 3), (0, 1)}))


def test_hit4():
    newfleet, ship = hit(0, 0, [(0, 0, True, 4, {(0, 1), (0, 2), (0, 3)}),
                                (9, 9, False, 1, set())])  # fourth final hit
    newfleet.sort()
    result = (newfleet, ship)
    assert result == ([(0, 0, True, 4, {(0, 1), (0, 2), (0, 3), (0, 0)}),
                       (9, 9, False, 1, set())],
                      (0, 0, True, 4, {(0, 1), (0, 2), (0, 3), (0, 0)}))


def test_hit5():
    # hit vertical ship
    newfleet, ship = hit(9, 9, [(0, 0, True, 4, {(0, 0), (0, 1), (0, 2),(0,3)}),
                                (8, 9, False, 2, set())])
    newfleet.sort()
    result = (newfleet, ship)
    assert result == ([(0, 0, True, 4, {(0, 0), (0, 1), (0, 2), (0, 3)}),
                       (8, 9, False, 2, {(9, 9)})],
                      (8, 9, False, 2, {(9, 9)}))


def test_hit6():
    # sink last ship
    newfleet, ship = hit(9, 9, [(0, 3, True, 4, {(0, 3), (0, 0), (0, 1), (0, 2)}), (8, 9, False, 2, {(8,9)})])
    newfleet.sort()
    result = (newfleet, ship)
    assert result == ([(0, 3, True, 4, {(0, 3), (0, 0), (0, 1), (0, 2)}),
                       (8, 9, False, 2, {(8, 9), (9, 9)})],
                      (8, 9, False, 2, {(8, 9), (9, 9)}))


def test_are_unsunk_ships_left1():  # input fleet -> output true or false
    full_fleet_sunk = [(0, 0, True, 4, {(0, 3), (0, 2), (0, 1), (0, 0)}),
                       (0, 5, True, 3, {(0, 7), (0, 6), (0, 5)}),
                       (2, 0, True, 3, {(2, 2), (2, 1), (2, 0)}),
                       (2, 4, True, 2, {(2, 5), (2, 4)}),
                       (2, 7, True, 2, {(2, 8), (2, 7)}),
                       (4, 0, True, 2, {(4, 1), (4, 0)}),
                       (4, 3, False, 1, {(4, 3)}),
                       (4, 5, True, 1, {(4, 5)}),
                       (4, 7, False, 1, {(4, 7)}),
                       (4, 9, True, 1, {(4, 9)})]
    # no ships hit
    s = [(0, 0, True, 4, set()),
         (0, 5, True, 3, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 2, set()),
         (2, 8, True, 2, set())]

    assert are_unsunk_ships_left(s) == True

def test_are_unsunk_ships_left2():
    # one ship hit not sunk
    s = [(0, 0, True, 4, {0, 3}),
         (0, 5, True, 3, set()),
         (2, 0, True, 3, set()),
         (2, 4, True, 2, set()),
         (2, 7, True, 2, set())]

    assert are_unsunk_ships_left(s) == True

def test_are_unsunk_ships_left3():
    # all ships hit not sunk
    s = [(0, 0, True, 4, {0, 3}),
         (0, 5, True, 3, {0, 6}),
         (2, 0, True, 3, {2, 2}),
         (2, 4, True, 2, {2, 5}),
         (2, 7, True, 2, {2, 7})]

    assert are_unsunk_ships_left(s) == True

def test_are_unsunk_ships_left4():
    # multiple ships sunk
    full_fleet_not_sunk = [(0, 3, True, 4, {(0, 3), (0, 2), (0, 1), (0, 0)}),
                           (0, 7, True, 3, {(0, 7), (0, 6), (0, 5)}),
                           (2, 2, True, 3, {(2, 2), (2, 1), (2, 0)}),
                           (2, 5, True, 2, {(2, 5), (2, 4)}),
                           (2, 8, True, 2, {(2, 8), (2, 7)}),
                           (4, 1, True, 2, {(4, 1), (4, 0)}),
                           (4, 3, False, 1, {(4, 3)}),
                           (4, 5, True, 1, {(4, 5)}),
                           (4, 7, False, 1, {(4, 7)}),
                           (4, 9, True, 1, set())]
    assert are_unsunk_ships_left(full_fleet_not_sunk) == True

def test_are_unsunk_ships_left5():
    full_fleet_sunk = [(0, 0, True, 4, {(0, 3), (0, 2), (0, 1), (0, 0)}),
                       (0, 5, True, 3, {(0, 7), (0, 6), (0, 5)}),
                       (2, 0, True, 3, {(2, 2), (2, 1), (2, 0)}),
                       (2, 4, True, 2, {(2, 5), (2, 4)}),
                       (2, 7, True, 2, {(2, 8), (2, 7)}),
                       (4, 0, True, 2, {(4, 1), (4, 0)}),
                       (4, 3, False, 1, {(4, 3)}),
                       (4, 5, True, 1, {(4, 5)}),
                       (4, 7, False, 1, {(4, 7)}),
                       (4, 9, True, 1, {(4, 9)})]
    # all ships hit (sunk)
    assert are_unsunk_ships_left(full_fleet_sunk) == False
