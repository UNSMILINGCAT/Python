import base64

st = "www.baidu.com"
ssr='ssr://MTAzLjExNC4xNjEuMTU4OjMwMTg6b3JpZ2luOmFlcy0yNTYtY2ZiOnBsYWluOmJuUmtkSFl1WTI5dC8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVwYXc1NXFFJmdyb3VwPTVZLXY1NVNv'
encoded = base64.encodebytes(bytes(st,'utf-8'))
print(encoded)
print(base64.encodebytes(bytes(ssr,'ascii')))
