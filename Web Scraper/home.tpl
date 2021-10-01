<!DOCTYPE html>
<html lang="en">
<head>
  <title>Web Scraper</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
   
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

</head>
<body>

<div class="container-fluid p-5 bg-primary text-white text-center">
  <h1> Stock Market Web Scraper</h1>
</div>
  
<div class="container">
  <h2>Top 10 Gaining Stocks In The US</h2>
  <p>Down below are the top 10 gaining stocks based on TradingView</p>
  <table class="table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Cost</th>
        <th> Up %</th>
        <th>Cost Change</th>
      </tr>
    </thead>
    <tbody>     
      <tr class="success">
        <td>{{row1_name}}</td>
        <td>{{row1_price}}</td>
        <td>{{row1_percent_change}}</td>
        <td>{{row1_price_change}}</td>
      </tr>
      <tr class="danger">
        <td>{{row2_name}}</td>
        <td>{{row2_price}}</td>
        <td>{{row2_percent_change}}</td>
        <td>{{row2_price_change}}</td>
      </tr>
      <tr class="info">
        <td>{{row3_name}}</td>
        <td>{{row3_price}}</td>
        <td>{{row3_percent_change}}</td>
        <td>{{row3_price_change}}</td>
      </tr>
      <tr class="warning">
        <td>{{row4_name}}</td>
        <td>{{row4_price}}</td>
        <td>{{row4_percent_change}}</td>
        <td>{{row4_price_change}}</td>
      </tr>
      <tr class="active">
        <td>{{row5_name}}</td>
        <td>{{row5_price}}</td>
        <td>{{row5_percent_change}}</td>
        <td>{{row5_price_change}}</td>
      </tr>
       <tr class="success">
        <td>{{row6_name}}</td>
        <td>{{row6_price}}</td>
        <td>{{row6_percent_change}}</td>
        <td>{{row6_price_change}}</td>
      </tr>
      <tr class="danger">
        <td>{{row7_name}}</td>
        <td>{{row7_price}}</td>
        <td>{{row7_percent_change}}</td>
        <td>{{row7_price_change}}</td>>
      </tr>
      <tr class="info">
        <td>{{row8_name}}</td>
        <td>{{row8_price}}</td>
        <td>{{row8_percent_change}}</td>
        <td>{{row8_price_change}}</td>
      </tr>
      <tr class="warning">
        <td>{{row9_name}}</td>
        <td>{{row9_price}}</td>
        <td>{{row9_percent_change}}</td>
        <td>{{row9_price_change}}</td>
      </tr>
      <tr class="active">
        <td>{{row10_name}}</td>
        <td>{{row10_price}}</td>
        <td>{{row10_percent_change}}</td>
        <td>{{row10_price_change}}</td>
      </tr>
    </tbody>
  </table>
</div>
</body>

<center><footer> source: https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/ </footer></center>
</html>