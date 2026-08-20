const form = document.getElementById("predictionForm");

const predictBtn = document.getElementById("predictBtn");
const btnText = document.querySelector(".btn-text");
const loader = document.getElementById("loader");

const predictionValue =
    document.getElementById("predictionValue");

const predictionMessage =
    document.getElementById("predictionMessage");

const apiStatus =
    document.getElementById("apiStatus");


function getValue(id) {
    return document.getElementById(id).value;
}


function getNumber(id) {
    return Number(getValue(id));
}


function buildPayload() {

    return {

        Order_Hour: getNumber("Order_Hour"),

        Day_of_Week: getValue("Day_of_Week"),

        Is_Weekend: getNumber("Is_Weekend"),

        Is_Festival: getNumber("Is_Festival"),

        Weather: getValue("Weather"),

        Pickup_Zone: getValue("Pickup_Zone"),

        Dropoff_Zone: getValue("Dropoff_Zone"),

        Vehicle_Type: getValue("Vehicle_Type"),

        Rider_Experience_Years:
            getNumber("Rider_Experience_Years"),

        Rider_Rating:
            getNumber("Rider_Rating"),

        Restaurant_Rating:
            getNumber("Restaurant_Rating"),

        Cuisine_Type:
            getValue("Cuisine_Type"),

        Order_Items:
            getNumber("Order_Items"),

        Restaurant_Load:
            getValue("Restaurant_Load"),

        Preparation_Time_Min:
            getNumber("Preparation_Time_Min"),

        Road_Distance_km:
            getNumber("Road_Distance_km"),

        Delivery_Distance_Category:
            getValue("Delivery_Distance_Category"),

        Traffic_Level:
            getValue("Traffic_Level"),

        Number_of_Signals:
            getNumber("Number_of_Signals"),

        Average_Speed_kmph:
            getNumber("Average_Speed_kmph"),

        Delivery_Priority:
            getValue("Delivery_Priority"),

        Order_Year:
            getNumber("Order_Year"),

        Order_Month:
            getNumber("Order_Month"),

        Order_Day:
            getNumber("Order_Day")
    };
}


function setLoading(isLoading) {

    if (isLoading) {

        predictBtn.disabled = true;

        btnText.textContent = "Analyzing order...";

        loader.style.display = "block";

        apiStatus.textContent = "Processing";

    } else {

        predictBtn.disabled = false;

        btnText.textContent =
            "Predict Delivery Time";

        loader.style.display = "none";
    }
}


function animatePrediction(targetValue) {

    const duration = 900;

    const startTime = performance.now();

    function update(currentTime) {

        const elapsed =
            currentTime - startTime;

        const progress =
            Math.min(elapsed / duration, 1);

        const eased =
            1 - Math.pow(1 - progress, 3);

        const current =
            targetValue * eased;

        predictionValue.textContent =
            current.toFixed(1);

        if (progress < 1) {

            requestAnimationFrame(update);

        } else {

            predictionValue.textContent =
                targetValue.toFixed(1);
        }
    }

    requestAnimationFrame(update);
}


function updateMessage(minutes) {

    if (minutes <= 45) {

        predictionMessage.textContent =
            "Fast delivery window. Route conditions look favorable.";

    } else if (minutes <= 75) {

        predictionMessage.textContent =
            "Moderate delivery window based on current order conditions.";

    } else if (minutes <= 110) {

        predictionMessage.textContent =
            "Longer delivery window. Traffic and route factors may contribute.";

    } else {

        predictionMessage.textContent =
            "High delivery time predicted. Expect significant route or traffic delays.";
    }
}


form.addEventListener("submit", async function (event) {

    event.preventDefault();

    setLoading(true);

    try {

        const payload = buildPayload();

        const response = await fetch(
            "/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(payload)
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Prediction request failed."
            );
        }


        const prediction =
            Number(
                data.predicted_delivery_time_minutes
            );


        animatePrediction(prediction);

        updateMessage(prediction);

        apiStatus.textContent = "Success";


    } catch (error) {

        console.error(error);

        predictionValue.textContent = "--";

        predictionMessage.textContent =
            error.message;

        apiStatus.textContent = "Error";


    } finally {

        setLoading(false);
    }

});
