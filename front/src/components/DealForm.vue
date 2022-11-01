<template>
    <div>
        <h3>Создание сделки</h3>
        <form @submit.prevent>
            <InputUI
              v-model.trim="deal.type"
              type="text"
              placeholder="Тип"/>
            <InputUI
              v-model.trim="deal.date_deal" 
              type="text"
              placeholder="Дата и время сделки"/>
            <InputUI
              v-model.trim="deal.counterpartry"
              type="text"
              placeholder="Контрагент"/>
            <InputUI
              v-model.trim="deal.delivery_point" 
              type="text"
              placeholder="Пункт поставки"/>
            <InputUI
              v-model.trim="deal.tool"
              type="text"
              placeholder="Инструмент"/>
            <InputUI
              v-model.trim="deal.delivery_start" 
              type="text"
              placeholder="Начало поставки"/>
            <InputUI
              v-model.trim="deal.delivery_end"
              type="text"
              placeholder="Конец поставки"/>
            <InputUI
              v-model.number="deal.volume" 
              type="text"
              placeholder="Объем, МВт"/>
            <InputUI
              v-model.number="deal.cost"
              type="text"
              placeholder="Цена, евро / МВт*ч"/>
            <ButtonUI @click="createDeal" class="btn">Создать</ButtonUI>
        </form>
    </div>
</template>
<script>
import ButtonUI from './UI/ButtonUI.vue';
import InputUI from './UI/InputUI.vue';

export default {
    components:{
        InputUI, ButtonUI
    },
    data(){
        return{
            deal: {
                type:"",
                date_deal:"",
                counterpartry:"",
                delivery_point:"",
                tool:"",
                delivery_start:"",
                delivery_end:"",
                volume:"",
                cost:"",
            }
        };
    },
    methods:{
        createDeal(){ 
            this.deal.id=Date.now();
            this.$emit("create", this.deal);
            console.log(this.deal)
            this.deal = {         
                type:'',
                date_deal:'',
                counterpartry:'',
                delivery_point:'',
                tool:'',
                delivery_start:'',
                delivery_end:'',
                volume:'',
                cost:''
        };
    }
    }
}
</script>
<style scoped>
form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
form>button{
    margin-top: 15px;
}
</style>