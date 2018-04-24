# Valohai Integration Examples

Here are examples how to manage files and data adapters in various ways on [Valohai machine learning platform][vh].

Archive datasets used in examples are uncompressed zip files.

* `numbers.zip` contains 22 files, all 200x200 pixel images in two formats (JPG and PNG).
* `edinburgh.zip` contains 3 files, all 1440x1080 JPG photographs.

```bash
zip -r0 numbers.zip numbers/
#  adding: numbers/ (stored 0%)
#  adding: numbers/0.jpg (stored 0%)
#  adding: numbers/0.png (stored 0%)
#  adding: numbers/1.jpg (stored 0%)
#  adding: numbers/1.png (stored 0%)
#  adding: numbers/2.jpg (stored 0%)
#  adding: numbers/2.png (stored 0%)
#  adding: numbers/3.jpg (stored 0%)
#  adding: numbers/3.png (stored 0%)
#  adding: numbers/4.jpg (stored 0%)
#  adding: numbers/4.png (stored 0%)
#  adding: numbers/5.jpg (stored 0%)
#  adding: numbers/5.png (stored 0%)
#  adding: numbers/6.jpg (stored 0%)
#  adding: numbers/6.png (stored 0%)
#  adding: numbers/7.jpg (stored 0%)
#  adding: numbers/7.png (stored 0%)
#  adding: numbers/8.jpg (stored 0%)
#  adding: numbers/8.png (stored 0%)
#  adding: numbers/9.jpg (stored 0%)
#  adding: numbers/9.png (stored 0%)
#  adding: numbers/empty.jpg (stored 0%)
#  adding: numbers/empty.png (stored 0%)
# => numbers.zip (17.6KB)

zip -r0 edinburgh.zip edinburgh/
#  adding: edinburgh/ (stored 0%)
#  adding: edinburgh/arthurs-seat.jpg (stored 0%)
#  adding: edinburgh/city.jpg (stored 0%)
#  adding: edinburgh/street.jpg (stored 0%)
# => edinburgh.zip (1.6MB)
```

[vh]: https://valohai.com/
