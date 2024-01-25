const fs = require('fs');
const Papa = require('papaparse');

// 定义转换函数
function convertCSVtoJSON(csvFilePath, jsonFilePath) {
  // 读取CSV文件内容
  fs.readFile(csvFilePath, 'utf8', function (err, data) {
    if (err) {
      console.error('Error reading CSV file:', err);
      return;
    }

    // 使用PapaParse解析CSV数据
    Papa.parse(data, {
      header: true,
      dynamicTyping: true,
      skipEmptyLines: true,
      complete: function (results) {
        // 解析完成后的回调函数，将JSON数据写入文件
        fs.writeFile(jsonFilePath, JSON.stringify(results.data, null, 2), function (err) {
          if (err) {
            console.error('Error writing JSON file:', err);
            return;
          }
          console.log(`Converted ${csvFilePath} to ${jsonFilePath}`);
        });
      }
    });
  });
}

// 调用转换函数，传入CSV文件路径和期望的JSON文件输出路径
convertCSVtoJSON('2021_1_monthly_sum.csv', '2021_1_monthly_sum.json');
