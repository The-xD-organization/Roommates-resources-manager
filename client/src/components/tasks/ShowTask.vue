<template>
    <div>
        <h5> /Obowiązek/ </h5>
        <hr>
        <p>Data utworzenia: </p>
        <p>Przypisana osoba: </p>
        <b-button variant="btn" class="m-1">
            Przypisz się
        </b-button>
        <b-button variant="btn" class="m-1">
            Zrobione
        </b-button>
    </div>
</template>

<script>
export default {
    name: 'ShowTask',
    props: {
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
</style>
