# 1. Technical requirements
# 2. Introduction to XPath and CSS selector
## 2.1. XPath
* Hãy cùng tìm hiểu cách sử dụng XPath qua tệp [`food.xml`](food.xml) dưới đây
```xml
<?xml version="1.0" encoding="UTF-8"?>
<menus>
  <food>
    <name>Butter Milk with Vanilla</name>
    <price>$3.99</price>
    <description>Rich tangy buttermilk with vanilla essence</description>
    <rating>5.0</rating>
    <feedback>6</feedback>
  </food>
  <food>
    <name>Fish and Chips</name>
    <price>$4.99</price>
    <description>Crispy fried Chips and Fish served with lemon and malt vinegar</description>
    <rating>5.0</rating>
    <feedback>10</feedback>
  </food>
  <food>
    <name>Egg Roll</name>
    <price>$3.99</price>
    <description>Fresh egg rolls filled with ground chicken, carrot, cabbage</description>
    <rating>4.0</rating>
    <feedback>8</feedback>
  </food>
  <food>
    <name>Pineapple Cake</name>
    <price>$3.99</price>
    <description>Crushed Pineapple mixed with vanilla, eggs and lemon juice</description>
    <rating>5.0</rating>
    <feedback>9</feedback>
  </food>
  <food>
    <name>Eggs and Bacon</name>
    <price>$5.50</price>
    <description>Served with rice and fresh fruit</description>
    <rating>4.5</rating>
    <feedback>4</feedback>
  </food>
  <food>
    <name>Orange Juice</name>
    <price>$2.99</price>
    <description>Fresh Orange juice served</description>
    <rating>4.9</rating>
    <feedback>10</feedback>
  </food>
</menus>
```
* Có thể sử dụng trang web [https://codebeautify.org/Xpath-Tester](https://codebeautify.org/Xpath-Tester) để kiểm tra XPath
* Ở đây ta thấy thẻ `<menus>` chứa nhiều thẻ `<food>` bên trong, để lấy tất các các thẻ `<food>` này, ta làm như sau:
  ![](images/03_00.png)
