<template >
    <tr>
        <td>{{deal.type}}</td>
        <td>{{deal.date_deal}}</td>
        <td>{{deal.counterpartry}}</td>
        <td>{{deal.delivery_point}}</td>
        <td>{{deal.tool}}</td>
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