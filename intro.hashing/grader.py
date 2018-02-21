#!/usr/bin/env python3

import base64
import binascii
import hashlib
import io

MESSAGE = b'\negg{a_true_d3t3ct1v3!}'
IMG_DATA = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAACE4AAAhOAFFljFgAAAAB3RJTUUH4gIKFS0HJoYN+gAAAv9JREFUKM8FwVtoHFUAANCZe+fOc2cf031mN+nmZVpI2sIGs6RGwVeCShFEpSJVRD/ip+CHogj990NB9MMvsf5og/hRbVNQU/BBaEva0ocxTbvZ7GSdZHd2Zndm7tw7dzyH/+zNFzlFG5/KU9exzF6Ao2RKVXQlpJGiqoXRYYHDXOhpGkoYmp7PgnwxpcUBtiwZQSMtp4WQxwNJEgtDhYRxiEUs7DkcxjwfAwBjxgRKmKSIjAOu7dpte6i+UF2o60mFj0KGPcbFNIpZt8N1HlLfw31ZCDGJKXGtbrJcqr33Ybkktle+3rp6Pez3/YAgTdXzhzNzJxIzdYQdYt4XAmdAaTy5tDj98mmycenKmffDfQ/wUqQjAUFmu6zR7t34M8ycr5x5tzxxDJ6slGtvvDDx1ONxa/Pu2WXbFUimqCQFSiJjvJR7os6rfBwxRP0Hl34VJ4/yqyufF8dTQZyOrly8/+13PQ+NvLo0UivLqSRlQCkPWZubzS/OJWXB9QO3D8DRp+d37jX2Hv4HItILuERGVIkJ07kQqI7Z8g/cfLnIG+luH6u6GDoEdK7/4Q3o7b9uyWPTIGaijJAkR4Q3b/yTrIxCTtr9fWN4JpfMQDtEfQYFbmsV7cP2esOcPzG19OSdny4IO0cKIDikwMb3F0VMsflvgBCHYf8A4wjCUyWjUBWhQNZ+XD/29jJCsb3+G9nZ3v7l2mDX6u21gSIfHNBW0xm4Ye3jj+ARqCuek30k7wz8vy9fPf7WOyOz9b3bzWbLJTiIKd1tBZhJ2ZnZ+bMfGM8s8l99+klv9fz84rBeSV9YuWcH8qOnX5uam/P3nYHV4QIfqJp2uGpMTEUxtVrb/Fbn1s9fntMaa489N0ZldWPD7JpO7vjC6LMvKSkDKAnA8YwXGCFe12IRgbVidXH5lTub9s0f1qojidrzs6XJISlyiFplWi4KacS4mDHiD8LA1xIpqN1tFscqJ18/9aAbXvvmcjkrj87OZDIq5BDNTiMQMxaHnsfCQEvokoj+BwyzhsLgoeO6AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTAyLTEwVDIxOjQ1OjA3LTA1OjAwfgA8MgAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wMi0xMFQyMTo0NTowNy0wNTowMA9dhI4AAAAASUVORK5CYII='


def get_problem(random):
    # generate salt
    salt = bytes(random.getrandbits(8) for _ in range(16))

    # generate image file
    img = base64.b64decode(IMG_DATA) + salt + MESSAGE
    h = hashlib.sha512(img).hexdigest().lower()

    return img, h


def generate(random):
    img, h = get_problem(random)
    return dict(files={
        'image.png': io.BytesIO(img)
    })


def grade(random, key):
    img, h = get_problem(random)
    if h in key.lower():
        return True, "Yay, you can hash!"
    return False, "Sorry, try again."
