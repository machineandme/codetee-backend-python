const EXTS = [".ada", ".b", ".b", ".c", ".c++", ".cc", ".cmake", ".cmd", ".cs", ".css", ".cxx", ".d", ".dart", ".diff", ".dmesg", ".docker", ".ex", ".g", ".go", ".gradle", ".groovy", ".hh", ".html", ".inf", ".jade", ".java", ".js", ".json", ".less", ".lisp", ".lua", ".m", ".php", ".phtml", ".rb", ".scala", ".scss", ".sql", ".swift", ".tf", ".toml", ".ts", ".twig", ".v", ".vala", ".vb", ".vim", ".xml", ".yaml", ".zsh"]
const FNFIR = ["abominable", "absolute", "absurd", "acceptable", "accurate", "actual", "adult", "advanced", "advantageous", "aged", "agitated", "ancient", "appalled", "approximate", "aromatic", "arrogant", "artificial", "astonished", "average", "awed", "bad", "baked", "basic", "bitter", "blunt", "boastful", "boring", "brave", "brief", "bright", "broad", "busy", "calculating", "calm", "can", "capable", "careless", "certain", "cheap", "cheerful", "clean", "cold", "competitive", "complete", "complex", "concave", "conditional", "confident", "conic", "considerate", "constant", "contented", "continuous", "convex", "cooked", "cool", "cooperative", "correct", "crazy", "creative", "cubic", "cunning", "curious", "damaged", "dangerous", "deaf", "decent", "deep", "defective", "dejected", "delightful", "depressed", "desirable", "difficult", "diligent", "disadvantageous", "distressed", "divorced", "doubtful", "dreamy", "dry", "early", "easy", "efficient", "emaciated", "emotional", "engaged", "enterprising", "equal", "erudite", "essential", "even", "exact", "excellent", "excessive", "excited", "exhausted", "expensive", "experienced", "faithful", "false", "fantastic", "far", "fat", "fearful", "final", "fine", "fragrant", "free", "frequent", "fresh", "fried", "friendly", "frightened", "full", "fuming", "future", "gifted", "glad", "good", "great", "greedy", "grown", "guilty", "haggard", "handsome", "happy", "hard", "harmful", "harmless", "healthy", "honest", "horizontal", "horrified", "hospitable", "hot", "huge", "humid", "hungry", "hurt", "hysterical", "ignorant", "illegal", "illogical", "imaginary", "important", "impudent", "inclined", "incomplete", "incorruptible", "industrious", "inexperienced", "inferior", "infrequent", "infuriated", "initial", "insignificant", "insufficient", "intact", "interesting", "invalid", "irritable", "late", "lazy", "lean", "little", "logical", "lonely", "long", "loud", "lovey", "low", "lucky", "mad", "married", "mature", "maximum", "mediocre", "minimum", "modest", "moved", "muffled", "naive", "narrow", "natural", "near", "necessary", "negative", "negligent", "nervous", "nice", "noisy", "normal", "numerous", "observant", "obsolete", "obstinate", "occasional", "occupied", "old", "optimistic", "optimum", "outgoing", "oval", "particular", "past", "peevish", "perfect", "periodical", "persistent", "pessimistic", "pleasant", "positive", "practical", "preceding", "precise", "pregnant", "preliminary", "present", "pretty", "previous", "profitable", "pungent", "purposeful", "quick", "quiet", "ragged", "rapid", "rare", "raw", "ready", "real", "recent", "rectangular", "redundant", "regular", "rejected", "relative", "reliable", "repulsive", "reserved", "respectful", "responsible", "rich", "robust", "rough", "round", "sad", "salty", "sarcastic", "satisfactory", "satisfied", "secondary", "self", "selfish", "separate", "serious", "shallow", "sharp", "shocked", "shocking", "short", "shy", "significant", "similar", "simultaneous", "single", "slim", "slow", "sly", "smelly", "smooth", "sociable", "soft", "sophisticated", "sorrowful", "sorry", "sour", "special", "specific", "spherical", "spoiled", "spoilt", "square", "stable", "standard", "startled", "stinking", "straight", "strange", "strong", "stuffed", "stunned", "sudden", "sufficient", "superfluous", "superior", "surprised", "sweet", "talented", "talkative", "tall", "tasteless", "terrified", "theoretical", "thick", "thin", "thirsty", "thorough", "tired", "tiresome", "tolerant", "touching", "tough", "traditional", "triangular", "true", "trusting", "typical", "ugly", "unattractive", "uneven", "unhappy", "uninterrupted", "unpleasant", "unprofitable", "upset", "urgent", "useful", "useless", "usual", "vacant", "valid", "vertical", "vigorous", "warm", "weak", "well", "wet", "wise", "wonderful", "woozy", "worried", "wrong", "young"]
const FNSEC = ["app", "module", "script", "example", "index", "style", "test", "view"]

function choose(choices) {
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}

function makeFileTypes() {
    let result = []
    for (let i = 0; i < 1; i++) {
        mr = Math.random()
        if (mr < .1) {
            let s = choose(FNSEC)
            s = s.charAt(0).toUpperCase() + s.slice(1)
            result.push(choose(FNFIR) + s + choose(EXTS))
        } else if (mr < .2) {
            result.push((choose(FNFIR) + "_" + choose(FNSEC) + choose(EXTS)).toUpperCase())
        } else {
            result.push(choose(FNFIR) + "_" + choose(FNSEC) + choose(EXTS))
        }
    }
    return result.join(", ")
}

let wap = new Vue({
    el: "#app",
    data: {
        fileType: makeFileTypes()
    }
})

setInterval(()=>{
    wap.fileType = makeFileTypes()
}, 2000)