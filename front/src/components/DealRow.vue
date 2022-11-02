<template >
    <tr>
        <td>{{deal.type.name}}</td>
        <td>{{deal.date_deal}}</td>
        <td>{{deal.counterparty.name}}</td>
        <td>{{deal.delivery_point.name}}</td>
        <td>{{deal.tool.name}}</td>
        <td>{{deal.delivery_start}}</td>
        <td>{{deal.delivery_end}}</td>
        <td>{{deal.volume}}</td>
        <td>{{deal.cost}}</td>
    </tr>
</template>
<script>
export default {
    props:{
        deal:{
            type:Object,
            required: true,
        }
    }
    
}
</script>
<style scoped>
td{
    text-align: left;
    padding:15px;
  }
td:first-child{
    padding-left: 25px;
  }
th:last-child{
    border: none;
  }
tr:nth-child(odd){
    background-color: #F2F7FC;
  }
</style>