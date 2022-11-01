<template>
  <div>
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
      <tr v-bind:key="row.id" v-for="row in rows">
        <td>{{row.type}}</td>
        <td>{{row.date_deal}}</td>
        <td>{{row.counterpartry}}</td>
        <td>{{row.delivery_point}}</td>
        <td>{{row.tool}}</td>
        <td>{{row.delivery_start}}</td>
        <td>{{row.delivery_end}}</td>
        <td>{{row.volume}}</td>
        <td>{{row.cost}}</td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  data(){
    return{
      rows:[
        { id:1,
          type:'esp',
          date_deal:'lorem ipsum',
          counterpartry:'lorem ipsum',
          delivery_point:'lorem ipsum',
          tool:'lorem ipsum',
          delivery_start:'lorem ipsum',
          delivery_end:'lorem ipsum',
          volume:'lorem ipsum',
          cost:'lorem ipsum'
        },
        { id:2,
          type:'efet',
          date_deal:'lorem ipsum 2',
          counterpartry:'lorem ipsum 2',
          delivery_point:'lorem ipsum 2',
          tool:'lorem ipsum 2',
          delivery_start:'lorem ipsum 2',
          delivery_end:'lorem ipsum 2',
          volume:'lorem ipsum 2',
          cost:'lorem ipsum 2'
        },
        { id:3,
          type:'esp',
          date_deal:'lorem ipsum 2',
          counterpartry:'lorem ipsum 3',
          delivery_point:'lorem ipsum 3',
          tool:'lorem ipsum 3',
          delivery_start:'lorem ipsum 3',
          delivery_end:'lorem ipsum 3',
          volume:'lorem ipsum 3',
          cost:'lorem ipsum 3'
        },
      ]
    }
  }
}
</script>
<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

tr:nth-child(odd){
  background-color: #F2F7FC;
}
table{
  max-width: 1374px;
  width: 100%;
  border-collapse: collapse;
  margin: auto;
}
td{
  text-align: left;
  padding: 5px 15px;
}
th{
  text-align: center;
  padding: 5px 15px;
  border-right: 1px solid #B9E4FF;
}
tr{
  padding: 5px;
}
th:first-child{
  padding-left: 25px;
}
td:first-child{
  padding-left: 25px;
}
th:last-child{
  border: none;
}
</style>