<template>
        <b-card
        variant="info"
        class="my-2"
        border-variant="info"
        :class="{done: task.is_done||doClicked}"
    >
        <h5> {{ task.description }} </h5>
        <hr>
        <p>Data utworzenia: {{ task.date_of_creation }}</p>
        <p v-if="task.assignee_name != null">Przypisana osoba: {{ task.assignee_name }} </p>
        <b-button
            v-else-if="asigneeClicked==false"
            variant="btn" class="m-1"
            @click="asigneeToTask()"
        >
            Przypisz się
        </b-button>
        <b-button
            v-if="task.is_done == false
                && task.assignee_name==$store.state.userData.username
                && doClicked==false"
            variant="btn" class="m-1"
            @click="doTask()"
        >
            Zrobione
        </b-button>
        <p v-if="asigneeClicked==true">Przypisałeś się!</p>
    </b-card>
</template>

<script>
export default {
    name: 'ShowTask',
    props: {
        task: Object,
    },
    data() {
        return {
            doClicked: false,
            asigneeClicked: false,
        };
    },
    methods: {
        doTask() {
            this.$store.dispatch('doTask', this.task.id);
            this.doClicked = true;
        },
        asigneeToTask() {
            this.$store.dispatch('asigneeToTask', this.task.id, this.task.assignee_name);
            this.asigneeClicked = true;
        },
    },
    mounted() {
        if (this.$store.state.userData === null) {
            this.$store.dispatch('getUserData');
        }
    },
};

</script>

<style scoped>
.btn{
    background-color:white;
    border-color: #17a2b8;
    color:#17a2b8;
}
.btn:hover{
    background-color: #17a2b8;
    color:white;
}
.done{
    border-color: gray!important;
    color: gray;
}
</style>
