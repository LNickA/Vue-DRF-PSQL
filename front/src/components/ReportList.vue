<template>
    <div v-show="reports.length > 0">
        <table>
            <tr>
              <th>Кредитный рейтинг</th>
              <th>Объем, тыс. куб. м</th>
              <th>Цена, долл. США / тыс. куб. м</th>
            </tr>
            <ReportRow
                v-bind:key="report.id"
                v-for="report in reports"
                :report="report" />
          </table>
    </div>
    <div v-show="reports.length === 0">
      <h3>Загрузка</h3>
    </div>
</template>
<script>
import ReportRow from "./ReportRow.vue";
export default {
    components: { ReportRow },
    props:{
        reports:{
            type:Array,
            required:true
        }
    },

}
</script>
<style scoped>
table{
    max-width: 1374px;
    width: 100%;
    border-collapse: collapse;
    margin: auto;
    margin-top: 15px;
    margin-bottom: 80px;
  }
th{
    text-align: left;
    padding:15px;
    border-right: 1px solid #B9E4FF;
  }
th:first-child{
    padding-left: 25px;
    max-width: 250px;
    width: 190px;
  }
th:nth-child(2){
  width: 190px;
  text-align: center;
}
th:last-child{
    border: none;
}
tr:nth-child(even){
    background-color: #fff;
  }
div>h3{
  text-align: center;
  margin-top: 15px;
  font-size: 18px;
}
</style>