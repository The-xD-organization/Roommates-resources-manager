<template>
    <b-container class="task-form">
        <b-row align-h="center">
            <b-col>
        <b-card title="Dodaj obowiązek"
            border-variant="info"
        >
        <form>
            <b-form-input
                class="my-2 form-style"
                placeholder="Opis"
                v-model="taskData.description"
            ></b-form-input>
            <b-button
                class="my-2 add-task-btn"
                block
                @click="sendTask()"
            >
                Wyślij
            </b-button>
        </form>
        <b-spinner v-if="$store.state.addNewTaskStatus === 0" variant="info"
        label="Spinning"></b-spinner>
        <p v-else-if="$store.state.addNewTaskStatus === 1">Wysłano</p>
        <p v-else-if="$store.state.addNewTaskStatus === -1">Wysyłanie nie powiodło się</p>
        <p v-else-if="areInputsEmpty">Nie możesz dodać pustego rachunku</p>
        </b-card>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name: 'AddTask',
    data() {
        return {
            taskData: {
                description: null,
            },
            areInputsEmpty: false,
        };
    },
    beforeDestroy() {
        this.$store.commit('setAddNewBillStatus', null);
    },
    methods: {
        sendTask() {
            if (this.taskData.description !== null) {
                this.areInputsEmpty = false;
                this.$store.dispatch('addNewTask', this.taskData);
            } else {
                this.areInputsEmpty = true;
            }
        },
    },
};

</script>

<style scoped>
.task-form{
    max-width: 400px;
    text-align: center;
    position: relative;
}
.add-task-btn{
    background-color: #17a2b8;
}
.form-style{
    border-color: #17a2b8;
}
</style>
