Exceptions
==========

BinanceRequestException
------------------------

Raised if a non JSON response is returned

This exception is used to handle cases where the response from the Binance API is not in JSON format,
which is expected for most API calls. It helps in identifying issues with the API response.

Example usage:

.. code:: python

    try:
        client.get_all_orders()  # Attempt to fetch all orders
    except BinanceAPIException as e:  # Catch specific Binance API exceptions
        print(e.status_code)  # Print the HTTP status code of the error
        print(e.message)  # Print the error message returned by the API

BinanceAPIException
-------------------

On an API call error a binance.exceptions.BinanceAPIException will be raised.

The exception provides access to the

- `status_code` - response status code
- `response` - response object
- `code` - Binance error code
- `message` - Binance error message
- `request` - request object if available

.. code:: python

    try:
        client.get_all_orders()
    except BinanceAPIException as e:
        print e.status_code
        print e.message
