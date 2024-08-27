# Eksempel på å sette opp et enkelt Power BI-dashbord som henter data fra en SQL-database
# 1. Koble Power BI til SQL-databasen.
# 2. Last inn data og lag interaktive visualiseringer.
# 3. Oppdater dashbordet automatisk basert på sanntidsdata.

# I D3.js:
<!DOCTYPE html>
<html>
<head>
  <script src="https://d3js.org/d3.v6.min.js"></script>
</head>
<body>
  <script>
    // Eksempel på enkel datavisualisering med D3.js
    const data = [30, 80, 45, 60, 20, 90, 50];

    const width = 500;
    const height = 150;
    const barWidth = width / data.length;

    const svg = d3.select('body')
      .append('svg')
      .attr('width', width)
      .attr('height', height);

    svg.selectAll('rect')
      .data(data)
      .enter()
      .append('rect')
      .

attr('width', barWidth - 2)
      .attr('height', d => d)
      .attr('x', (d, i) => i * barWidth)
      .attr('y', d => height - d)
      .attr('fill', 'teal');
  </script>
</body>
</html>