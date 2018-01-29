import time

class PhoneRouter:
    # Router can be used to check prices of phone calls based on phone number

    def __init__(self):
        self.route_dict = {}

    def add_route(self, route):
        # Add new route to route dictionary
        route = route.split(',')
        # Check if route already in dict. If so assign the smallest price
        if route[0] in self.route_dict:
            if float(route[1]) > self.route_dict[route[0]]:
                return
        self.route_dict[route[0]] = float(route[1])

    def add_route_text_file(self, file_name):
        # Add multiple routes from text file
        with open(file_name) as text_file:
            for line in text_file:
                self.add_route(line)

    def check_for_route(self, route_key):
        # Checks if route is present in route dictionary
        if route_key in self.route_dict:
            return self.route_dict[route_key]
        return None

    def check_phone_number(self, phone_number):
        # Checks phone number for route cost
        phone_number = phone_number[:-2]
        route_key = phone_number
        while route_key != '+':
            call_price = self.check_for_route(route_key)
            if call_price is not None:
                return phone_number + ',' + str(call_price)
            route_key = route_key[:-1]
        return phone_number + ',' + str(None)

    def check_phone_numbers_text_file(self, file_name, result_file="router_results.txt"):
        # Check multiple phone numbers from text file
        # Writes result to result_file text file
        with open(file_name) as read_file:
            write_file = open(result_file, 'w')
            for line in read_file:
                result = self.check_phone_number(line)
                write_file.write(result + "\n")


def scenario_2():
    print("Scenario 2: 106k routes; 1k phone numbers")

    # Define text files
    route_file = "route-costs-106000.txt"
    phone_number_file = "phone-numbers-1000.txt"
    result_file = 'results-2.txt'

    # Initialize router
    phone_router = PhoneRouter()
    phone_router.add_route_text_file(route_file)

    # Search for numbers
    phone_router.check_phone_numbers_text_file(phone_number_file, result_file)


def scenario_3():
    print("Scenario 3: 10mil routes; 10k phone numbers")

    # Define text files
    route_file = "route-costs-10000000.txt"
    phone_number_file = "phone-numbers-10000.txt"
    result_file = 'results-3.txt'

    # Initialize router
    phone_router = PhoneRouter()
    phone_router.add_route_text_file(route_file)

    # Search for numbers
    phone_router.check_phone_numbers_text_file(phone_number_file, result_file)


def main():
    print(" ")
    start_time = time.time()
    scenario_2()
    end_time = time.time()
    print("Run time:", end_time - start_time)
    print("--------")


if __name__ == "__main__":
    main()
