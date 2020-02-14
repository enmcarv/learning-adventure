/*
1. Instantiate new instance of XHR Object 
2. Set on readystatechange callback 
3. Specify action (HTTP), usually specify URL 
4. Send request
*/
const url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'

function getLocationData() {
    const dataReq = new XMLHttpRequest();

    dataReq.onreadystatechange = function() {
        if (dataReq.readyState === 4 && dataReq.status === 200) {
            let nationData = JSON.parse(dataReq.responseText);
            nationData = nationData.data
            // console.log(nationData)
            nationData.forEach((nation) => {
                const fullInfo = `In the ${nation.Nation}, in the year ${nation.Year}, the population was ${nation.Population}`;
                console.log(fullInfo)
            })
        }
    };
    dataReq.open('GET', url);
    dataReq.send();
}

getLocationData();
