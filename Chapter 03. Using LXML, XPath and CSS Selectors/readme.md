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
* Ở đây ta thấy thẻ `<menus>` chứa nhiều thẻ `<food>` bên trong, để lấy tất các các thẻ `<food>` này, thì XPath-expression của chúng ta là:
  ```xpath
  //food
  ```
  ![](images/03_00.png)

* Để lấy tất cả các thẻ `<price>`, thì XPath-expression là:
  ```xpath
  //food/price
  ```
  ![](images/03_01.png)

* Dưới đây là các XPath-expression mà hay sử dụng:
  |XPath-expression|Mô tả|
  |-|-|
  |`//<tag>`|Chọn tất cả các thẻ `<tag>` trong tài liệu bất kể chúng nằm ở đâu, [ví dụ](images/03_00.png).|
  |`//*`|Chọn tất cả các thẻ trong tài liệu, [ví dụ](images/03_04.png).|
  |`*`|Chọn tất cả các thẻ, [ví dụ](images/03_03.png).|
  |`//food/name|//food/price`|Chọn tất cả thẻ `<name>` và `<price>` dc tìm thấy trong các thẻ `<food>`, [vi dụ](images/03_02.png).|
  |`//food/name`|Chọn tất cả thẻ `<name>` nằm bên trong thẻ `<food>`, [ví dụ](images/03_05.png).|
  |`//food/name/text()`|Lấy content của tất cả các thẻ `<name>` lồng bên trong thẻ `<food>`, [ví dụ](images/03_06.png).|
  |`//food/name|//rating`|Lấy tất cả thẻ `<rating>` hoặc thẻ `<name>` nằm lồng trong thẻ `<food>`, [ví dụ](images/03_07.png).|
  |`//food[1]/name`|Lấy thẻ `<name>` trong thẻ `<food>` đầu tiên tìm dc, [ví dụ](images/03_08.png).|
  |`//food[feedback<9]`|Lấy tất cả thẻ `<food>` mà có thẻ `<feedback>` nằm lồng bên trong nó nhỏ hơn 9, [ví dụ](images/03_09.png).|
  |`//food[feedback<9]/name`|Lấy tất cả thẻ `<name>` nằm lồng trong các thẻ `<food>` có thẻ `<feedback>` lồng bên trong nhỏ hơn 9, [ví dụ](images/03_10.png).|
  |`//food[last()]/name`|Chọn thẻ `<name>` lồng trong thẻ `<food>` cuối cùng, [ví dụ](images/03_11.png).|
  |`//food[last()]/name/text()`|Lấy content của thẻ `<name>` lồng trong thẻ `<food>` cuối cùng, [ví dụ](images/03_12.png).|
  |`sum(//food/feedback)`|Lấy tổng của tất cả thẻ `<feedback>` lồng trong thẻ `<food>`, [ví dụ](images/03_13.png).|
  |`//food[rating>3 and rating<5]/name`|Lấy tất cả thẻ `<food>` có thẻ `<rating>` lồng bên trong nằm trong khoảng $[3, 5]$, [ví dụ](images/03_14.png).|
  |`//food/name[contains(.,"Juice")]`|Chọn các thẻ `<name>` có chứa chuổi '**Juice**' nằm lồng trong thẻ `<food>`, [ví dụ](images/03_15.png).|
  |`//food/description[starts-with(.,"Fresh")]/text()`|Lấy content của các thẻ `<description>` bắt đầu bằng chuổi '**Fresh**' nằm lồng trong thẻ `<food>`, [ví dụ](images/03_16.png).|
  |`//food/description[starts-with(.,"Fresh")]`|Chọn các thẻ `<description>` bắt đầu bằng chuổi '**Fresh**' nằm lồng trong thẻ `<food>`, [ví dụ](images/03_17.png).|
  |`//food[position()<3]` <mark>**(XPath đánh số từ 1, ko phải từ 0)**</mark>|Chọn hai thẻ `<food>` đầu tiên, [ví dụ](images/03_18.png).|

<hr>

* Tiếp theo, ta có file [`books.xml`](books.xml) như sau:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<books>
   <book id="1491946008" price="47.49">
      <author>Luciano Ramalho</author>
      <title>Fluent Python: Clear, Concise, and Effective Programming</title>
   </book>
   <book id="1491939362" price="29.83">
      <author>Allen B. Downey</author>
      <title>Think Python: How to Think Like a Computer Scientist</title>
   </book>
</books>
```

* Giả sử chúng ta cần truy cập vào thẻ có thuộc tính như ví dụ này chẳng hạn `id="1491946008"`, thì XPath cũng hộ trợ các expression để làm điều này:
  |XPath-expression|Mô tả|
  |-|-|
  |`//book/@price`|Chọn thuộc tính `price` từ thẻ `<book>`, [ví dụ](images/03_19.png).|
  |`//book`|Chọn tất cả thẻ `<book>`, [ví dụ](images/03_20.png).|
  |`//book[@price>30]`|Chọn các thẻ `<book>` mà có thuộc tính `price` lớn hơn 30, [ví dụ](images/03_21.png).|
  |`//book[@price<30]/title`|Lấy thẻ `<title>` từ các thẻ `<book>` mà có thuộc tính `price` lớn hơn 30, [ví dụ](images/03_22.png).|
  |`//book/@id`|Chọn thuộc tính `id` từ tất cả các thẻ `<book>`, [ví dụ](images/03_23.png).|
  |`//book[@id=1491939362]/author`|Chọn thẻ `<author>` của thẻ `<book>` có thuộc tính `id` bằng $1491939362$, [ví dụ](images/03_24.png).|

## 2.2. CSS Selectors
* Đối với CSS Selector có thể dùng trang web này [https://try.jsoup.org](https://try.jsoup.org).
* Giả sử có trang [`page.html`](page.html) như sau:
```html
<html>
  <head>
    <title>CSS Selectors: Testing</title>
    <style>
      h1 {
        color: black;
      }
      .header,
      .links {
        color: blue;
      }
      .plan {
        color: black;
      }
      #link {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1>Main Title</h1>
    <p class="”header”">Page Header</p>
    <div class="links">
      <a class="plan" href="*.pdf">Document Places</a>
      <a id="link" href="mailto:xyz@domain.com">Email Link1!</a>
      <a href="mailto:abc@domain.com">Email Link2!</a>
    </div>
  </body>
</html>
```

### 2.2.1. Element selectors
|CSS query|Mô tả|
|-|-|
|`h1`|Lấy tất cả các thẻ `<h1>`, [ví dụ](images/03_25.png).|
|`a`|Lấy tất cả các thẻ `<a>`, [ví dụ](images/03_26.png).|
|`*`|Lấy tất cả các thẻ tồn tại trong tài liệu, [ví dụ](images/03_27.png).|
|`body *`|Lấy tất cả các thẻ nằm trong thẻ `<body>`, [ví dụ](images/03_28.png).|
|`div a`|Lấy tất cả các thẻ `<a>` nằm bên trong các thẻ `<div>`, [ví dụ](images/03_29.png).|
|`h1+p`|Lấy tất cả thẻ `<p>` mà là **em** (em là cùng cấp đó mấy ba) của thẻ `<h1>`, [ví dụ](images/03_30.png).|
|`h1~p`|Lấy tất cả thẻ `<p>` mà có **chị** là thẻ `<h1>`, [ví dụ](images/03_31.png).|
|`h1,p`|Lấy tất cả các thẻ `<h1>` và `<p>`, [ví dụ](images/03_32.png).|
|`div>a`|Lấy tất cả thẻ `<a>` mà là **con** (con nha, ko phải cháu) của thẻ `<div>`, [ví dụ](images/03_33.png).|

### 2.2.2. ID and class selectors
|CSS query|Mô tả|
|-|-|
|`.header`|Chọn tất cả các thẻ có `class=header`.|
|`.plan`|Chọn tất cả các thẻ có `class=plan`.|
|`div.links`|Chọn tất cả các thẻ `<div>` có `class=link`.|
|`#link`|Chọn thẻ có `id=link`.|
|`a#link`|Chọn thẻ `<a>` có `id=link`.|
|`a.plan`|Chọn thẻ `<a>` có `class=plan`.|

### 2.2.3. Attribute selectors
|CSS query|Mô tả|
|-|-|
|`a[href*="domain"]`|Chọn các thẻ `<a>` mà có chuổi con là '**domain**' tồn tại bên trong thuộc tính `href`, ví dụ `<a id="link" href="mailto:xyz@domain.com">Email Link1!</a><a href="mailto:abc@domain.com">Email Link2!</a>`|
|`a[href*="domain"]`|Chọn các thẻ `<a>` có thuộc tính `href` bắt đầu bằng một chuổi con la '**mailto**'.|
|`a[href$="pdf"]`|Chọn các thẻ `<a>` có thuộc tính `href` kết thúc bằng chuổi con là '**pdf**'.|
|`[href~=do]`|Chọn các thẻ có thuộc tính `href` chứa chuổi con '**do**' bên trong.|
|`[class]`|Chọn các thẻ có khai báo thuộc tính `class` bên trong.|
|`[class=plan]`|Chọn các thẻ có thuộc tính `class=plan`.|

### 2.2.4. Pseudo selectors
|CSS query|Mô tả|
|-|-|
|`a:gt(0)`|Lấy tất cả các thẻ `<a>` có index lớn hơn $0$.|
|`a:eq(2)`|Lấy the `<a>` tại index bằng $2$.|
|`a:first-child`|Lấy các thẻ `<a>` là thẻ con đầu tiên của một thẻ nào đó.|
|`a:last-child`|Lấy các thẻ `<a>` là thẻ con cuối cùng của một thẻ nào đó.|
|`a:last-of-type`
|`:not(p)`|Lấy tất cả các thẻ trừ thẻ `<p>`.|

# 3. Using web browser developer tools for accessing web content
# 4. Scraping using lxml, a Python library
## 4.1. `lxml` by examples
### 4.1.1. Example 1 – reading XML from file and traversing through its elements
