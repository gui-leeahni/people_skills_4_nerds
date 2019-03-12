@sametmax i hear you, and i share the same pain.

The pain you feel is from using 'bleeding edge' stuff and ideas. I prefer this. Safe spaces (approved by leftist government) are not for me. I am very gratefull for alternatives, and i learned much from them. Even if i didnt use trio (yet), it was very good for me to learn some ideas from it.

 @njsmith
Member
njsmith commented on Aug 23, 2018
@alekibango I'm not sure what you think "safe space" means or why you're injecting comments about governments into a discussion about async library ecosystems, but please do review our code of conduct.

@sametmax Sorry I lost track of this question. To answer briefly and belatedly: You're right that splitting the ecosystem is a serious thing to do, and I thought hard before starting trio for this reason. It's a valid question. But hopefully from a year later it's clearer why I did it: trio's a fundamentally new and different approach, and the productivity benefits IME are large enough that trio has some chance of becoming the de facto standard (e.g., the 40 line happy eyeballs). I've taken this seriously from the start, and tried to grow a project and community commensurate with that task. Of course it's also possible that it won't – but if so the project still won't have been a waste, because we've been learning a tremendous amount about what it takes to make trio's theoretical ideas work in a real, practical system – things we couldn't have learned without actually doing it! – and now other projects like asyncio are studying us to learn from that experience. And in the mean time, the trio community tries to contribute back to the larger python async ecosystem wherever possible (e.g. async_generator, sphinxcontrib-trio, h11, ...), and we're working on projects to directly bridge the gap like trio-asyncio, sniffio, adding support for multiple async backends to urllib3...

Is that enough that we help more than we hurt? Well, I've done my best to make sure it is, but you'll have to judge for yourself.

 @njsmith njsmith closed this on Aug 23, 2018
@alekibango
alekibango commented on Sep 11, 2018
@njsmith, i am sorry if i sounded wrong.

Freedom to think and to search for happinness always leads to mupltiple paths. It is inevitable. All those new asyncio libraries are still somewhat 'bleeding edge' for general public. Living on the edge means living a dangerous and/or unusual everyday life.

Safe spaces on the other hand are by definition without new/dangerous/conflicting ideas. But real progress is impossible without some level of freedom, conflict and its resolution.

I really meant to say something like this: "I would love you to embrace the nature of living on the edge. It hurts, yes. Train hard, never quit. Fight the chaos and win. For you and for all of us. It is worth it. If we all used only one coding language and its standard library, life would be no fun. Both curio and trio helped me a lot! They surely didnt hurt me."

 @python-trio python-trio locked as off topic and limited conversation to collaborators on Sep 11, 2018
@njsmith
Member
njsmith commented on Sep 12, 2018
@Fuyukai Thanks.

@alekibango There's something exciting about the vision of new ideas coming out of violent struggle, isn't there? It's like the slogans in Nike ads – that stuff sells! But it doesn't match my experience. "Safe spaces" were invented as a tool for radical political organizing around issues like women's and LGBT rights. Developing new ways of thinking is difficult, especially when they go against the mainstream; new ideas start out fragile and flawed and need space to grow up a bit before they can be properly evaluated. It's like starting out new seedlings in a greenhouse so they can grow up a bit before being exposed to the outside weather.

I appreciate your enthusiasm, but Trio started as a project to distract me when I was sick and exhausted; if it had hurt, if I had to "train hard", "fight the chaos", then it wouldn't exist, because I just didn't (and don't) have the energy. The reason it exists as a separate project from asyncio, with a strong code of conduct and contributor guidelines, is exactly because its ideas need a safe space for experimentation and learning to happen. There's no war between trio and asyncio – in fact, I'm sitting next to the lead maintainers for asyncio and aiohttp right now; we're all working on the same problems, and learning from each other as we go. It's possible to engage with complex and controversial issues in a humane and thoughtful way; in fact, it's the only way the really works.

Anyway, this is getting way off-topic, so let's let this thread end here.
