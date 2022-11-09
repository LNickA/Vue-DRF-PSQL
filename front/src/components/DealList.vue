<template>
    <div v-show="deals.length > 0">
        <table>
            <tr>
              <th>Тип</th>
              <th>Дата и время сделки</th>
              <th>Контрагент</th>
              <th>Пункт поставки</th>
              <th>Инструмент</th>
              <th>Начало поставки</th>
              <th>Конец поставки</th>
              <th>Объем, МВт</th>
              <th>Цена, евро / МВт*ч</th>
            </tr>
            <DealRow
                v-bind:key="deal.id"
                v-for="deal in deals"
                :deal="deal" />
          </table>
    </div>
    <div v-show="deals.length === 0">
      <h3>Загрузка</h3>
    </div>
</template>
<script>
import DealRow from "./DealRow.vue"

export default {
    components: {DealRow},
    props:{
        deals:{
            type:Array,
            required:true
        }
    }
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
    padding: 15px;
    border-right: 1px solid #B9E4FF;
  }
tr{
    padding: 5px;
  }
th:first-child{
    padding-left: 25px;
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