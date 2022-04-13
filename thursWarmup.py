#!/usr/bin/env python3

import random

def apigrabber():
    status_codes = [200, 302, 307, 401, 403, 404, 418, 502]
    x = random.choice(status_codes)
    
    return x
    
def main():
    # all of your code will be written in the main function!
    apigrabber()
    
main()