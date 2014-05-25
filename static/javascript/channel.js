// Define drag beavior
        var drag = d3.behavior.drag()
            .on("drag", dragmove);

        function dragmove(d) {
            x1 = d3.event.x - x0;
            y1 = d3.event.y - y0;
            x0 = x1;
            y0 = y1;
            d3.selectAll("#moveable").attr("transform", "translate(" + x1 + "," + y1 + ")");

        }

        function click(){
            // Ignore the click event if it was suppressed
            if (d3.event.defaultPrevented) return;

            // Extract the click location\
            var point = d3.mouse(this)
            , p = {x: point[0], y: point[1] };

            // Append a new point
            for (channel in obj) {
                var image = svg.append("svg:image")
                .attr("width", circle_radius)
                .attr("height", circle_radius)
                .attr("x", i + circle_radius * 1.1 - circle_radius / 2)
                .style("position", "absolute");
            }
        }

        function mouseDown() {
            var point = d3.mouse(this);
            x0 = point[0];
            y0 = point[1];
        }

        function hover(){
            var point = d3.mouse(this);
            this.attr("x", point[0] - x0 - circle_radius / 2)
            .attr("y", point[1] - y0 - circle_radius / 2);
        }

        function exitHover(){
            this.transition()
            .delay(1000)
            .style("opacity", 1.0);
        }