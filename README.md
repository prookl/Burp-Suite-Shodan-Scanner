# Burp Suite Shodan Scanner 

Shodan Scanner adds enumeration capabilities on a target in Burp Suite. The scanner leverages the Shodan REST API to retrieve the following information from a target:

* Organization Name
* IP
* Location
* Open Ports

## Usage

Right-click any host or IP in Burp Suite and Select `Scan with Shodan`. The results will be in the extender tab under the Output sub tab. 

## Installation

Install this script like any other extension from the `Extender` tab, `open Burp Suite -> Extender -> Add -> path to file`. This scanner is written in Python, be sure to use Standalone Jython in Burp Suite. Download the latest [here](https://www.jython.org/download).

Lastly an API key from Shodan will be needed to make the API calls. 
