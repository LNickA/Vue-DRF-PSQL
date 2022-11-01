<template>
    <div v-show="counterpartys.length > 0">
        <table>
            <tr>
              <th>Контрагенты</th>
              <th>Цена закрытия</th>
            </tr>
            <CounterPartyRow
                v-bind:key="counterparty.id"
                v-for="counterparty in counterpartys"
                :counterparty="counterparty" />
          </table>
    </div>
    <div v-show="counterpartys.length === 0">
      <h3>Нет записей</h3>
    </div>
</template>
<script>
import CounterPartyRow from "./CounterPartyRow.vue";

export default {
    components: { CounterPartyRow },
    props:{
        counterpartys:{
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
    padding:15px;
    border-right: 1px solid #B9E4FF;
  }
th:first-child{
    padding-left: 25px;
    max-width: 250px;
    width: 250px;
  }
th:last-child{
    border: none;
}
tr:nth-child(even){
    background-color: #fff;
  }
</style>