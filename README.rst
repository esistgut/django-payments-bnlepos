django-payments-bnlepos
=======================

A django-payments backend for the BNL POSitivity (BNP Paribas) e-POSitivity virtual POS payment gateway.



Parameters
----------

* **store_id** : Store ID assigned by BNL Positivity.

* **shared_secret** : Shared Secret assigned by BNL Positivity.

* **endpoint** (default='https://test.ipg-online.com/connect/gateway/processing'): The e-POSitivity endpoint, should be 'https://test.ipg-online.com/connect/gateway/processing' for the test environment and 'https://www.ipg-online.com/connect/gateway/processing' for the production environment.

* **currency** (default='978'): Currency ISO code. The only accepted value is '978', ISO code for EURO.


Usage example
----------

Test configuration using default testing parameters:

.. code-block:: python

  PAYMENT_VARIANTS = {
      'bnlepos': ('payments_bnlepos.BNLePOSProvider', {
         'store_id': '10012345678',
         'shared_secret': 'HZ4qjxXs5e',
         'endpoint': 'https://test.ipg-online.com/connect/gateway/processing'}),
  }
