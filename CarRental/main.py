from CarRental.models.cab import Cab
from CarRental.models.location import Location
from CarRental.models.rider import Rider
from CarRental.service.trip_service import TripService

if __name__ == '__main__':
    rider_1 = Rider("1","rohan")
    rider_2 = Rider("2","saurav")
    rider_3 = Rider("3","vishal")




    cab_1 = Cab("1","msd")
    cab_2 = Cab("2", "kohli")

    location_1 = Location(100,200)
    location_2=  Location(200,100)

    trip_service = TripService()
    trip_service.register_rider(rider_1)
    trip_service.register_rider(rider_2)
    trip_service.register_rider(rider_3)

    trip_service.register_cab(cab_1)
    trip_service.update_cab_location(cab_1,location_1)

    trip_service.register_cab(cab_2)
    trip_service.update_cab_location(cab_2,location_2)

    trip_1  = trip_service.book_cab(rider_1,Location(200,300),Location(300,400))
    print(trip_1)

    trip_2 = trip_service.book_cab(rider_2,Location(200,300),Location(300,400))
    print(trip_2)

    try:
        trip_3 = trip_service.book_cab(rider_3,Location(200,300),Location(300,400))
    except Exception as e:
        print(e)

    trip_service.end_trip(trip_1.id)
    trip_3 = trip_service.book_cab(rider_3, Location(200, 300), Location(300, 400))
    print(trip_3.price)

    trip_service.end_trip(trip_3.id)
    trip_4 = trip_service.book_cab(rider_1, Location(200, 300), Location(300, 400))
    print(trip_4)

    print(trip_service.get_all_trip_by_rider(rider_1))
    print(trip_service.get_all_trip_by_rider(rider_2))



