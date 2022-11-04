<template >
    <tr @click="$router.push(`/counterparty/${counterparty.id}`)">
        <td>{{counterparty.name}}</td>
        <td>{{counterparty.score}}</td>
    </tr>
</template>
<script>
export default {
    props:{
        counterparty:{
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
tr:hover{
    background-color: #DEF2FF !important;
    cursor: pointer;
}
</style>