# PyVin - Retrieve Vehicle Information with Ease

**PyVin** is a straightforward Python package designed for fetching detailed vehicle information using Vehicle Identification Numbers (VINs) from the [National Highway Traffic Safety Administration (NHTSA)](https://www.nhtsa.gov/).

## Features

- **Simple to Use:** PyVin offers a user-friendly API that makes retrieving vehicle information as easy as a breeze.

- **Self-Contained:** PyVin does not rely on external packages or libraries, ensuring a lightweight and hassle-free installation process.

- **Open Source:** PyVin is an open-source project, which means you can contribute, modify, or customize it to suit your needs.

## Installation

Installing PyVin is a straightforward process using `setup.py`.

1. Clone the PyVin repository from GitHub:

```bash
git clone https://github.com/yourusername/pyvin.git
```
   
2. Navigate to the project directory:

```bash
cd pyvin
```

3. Install PyVin using `setup.py`:

```bash
python setup.py install
```

## Usage 

PyVin can extract whichever attributes are stored in the [National Highway Traffic Safety Administration (NHTSA)](https://www.nhtsa.gov/)
records for the vehicle.

Note: Record attributes are inconsistent.


## Example Usage 

Here's a simple example of how you can use PyVin to retrieve vehicle information:

``` python
import pyvin as pv 
# Single VIN lookup
vin = '1FDKF37G2VEB00330'

vehicle = pv.Vehicle(vin)
vehicle.display()

print(vehicle.model, vehicle.model_id)
# F-350 1806
```

``` python 
# Batch VIN lookup (Seperated on commas) 
vins = '1FDKF37G2VEB00330, 4USBU33577LW50386, KMHDB8AE3CU100820'

vehicles = pv.Vehicles(vins)
for vehicle in vehicles:
    vehicle.display()
```

## License 
PyVin is released under the MIT License.

## Acknowledgments
- https://github.com/h3/python-libvin

## References 
- https://randomvin.com/
- https://en.wikipedia.org/wiki/Vehicle_identification_number
