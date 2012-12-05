use agg
db.zips.aggregate([{
    $match: {
        state: "NY"
    }
}, {
    $group: {
        _id: "$city",
        population: {
            $sum: "$pop"
        },
        zip_codes: {
            $addToSet: "$_id"
        }
    }
}])



db.zips.aggregate([{
    $match: {
        $or: [{
            state: "NY",
            pop: {
                $gt: 25000
            }
        }]
    }
}, {
    $group: {
        _id: "$state",
        avg_pop: {
            $avg: "$pop"
        }
    }
}])



db.zips.aggregate([
{$unwind:"$scores"},

{
    $match: {
        $or: [{
            "$scores.type": "exam",
        }, {
            "$scores.type": "homework"
        }]
    }
}, {
    $group: {
        _id: "$student_id",
        avg_score: {
            $avg: "$scores.score"
        }
    }
}])


