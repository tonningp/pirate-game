#!/usr/bin/env python3

questions = [
{"question":"Who played the female lead in the 1942 film Casablanca?","answer":"Ingrid Bergman"}
,
{"question":"What do letters in the the acronym SCUBA stand for?","answer":"Self-Contained Underwater Breathing Apparatus"}
,
{"question":"In what year did the Houston Texans join the NFL?","answer":"2002"}
,
{"question":"SpaceX was founded by what South African-born inventor?","answer":"Elon Musk"}
,
{"question":"186,282 miles per second is the speed of what in a vacuum?","answer":"Light"}
,
{"question":"How many castaways were there on the American sitcom Gilligan's Island?","answer":"Seven"}
,
{"question":"What was the name of the Eminem single that set the world's record in 2013 for the most words used in a song?","answer":"Rap God"}
,
{"question":"And to think I saw it on Mulberry Street was the first book published by which children's author?","answer":"Dr. Seuss (Theodor Seuss Geisel)"}
,
{"question":"Who is the only head basketball coach to win both an NCAA national championship and an NBA title?","answer":"Larry Brown"}
,
{"question":"What is the name for a meat dish made from finely chopped raw beef often served with onion, capers, seasonings and raw egg?","answer":"Steak tartare"}
,
{"question":"What is the acronym for the intergovernmental military alliance based on the North Atlantic Treaty, signed in 1949?","answer":"NATO"}
,
{"question":"What was the name of the currency used in Spain before the euro?","answer":"Pesetas"}
,
{"question":"Tyler Durden is a ficitional character appearing as the central protagonist and antagonist in what 1999 American film?","answer":"Fight Club"}
,
{"question":"The Van Gogh museum is located in what European capital city?","answer":"Amsterdam"}
,
{"question":"What is the common name for the third and final set of molars that most people develop?","answer":"Wisdom Teeth"}
,
{"question":"To be legally sold as bourbon, a whiskey's mash must contain at least 51% of what grain?","answer":"Corn"}
,
{"question":"Released in 1992, what is the best selling soundtrack album of all time?","answer":"The Bodyguard"}
,
{"question":"What was the name of the gorilla that was shot and killed at the Cincinnati zoo in 2016 after a three-year old boy fell into the enclosure?","answer":"Harambe"}
,
{"question":"What is the most common type of pitch thrown by pitchers in baseball?","answer":"Fastball"}
,
{"question":"Who played lead guitar for the British rock band Queen?","answer":"Brian May"}
,
{"question":"Sequoia National Park is located in which U.S. state?","answer":"California"}
,
{"question":"The avocado is a tree that is thought to have originated in what country?","answer":"Mexico"}
,
{"question":"Which planet in our solar system has an axis that is titled by 98 degrees?","answer":"Uranus"}
,
{"question":"What is the name for the unit of measurement of power that is roughly equal to 746 watts?","answer":"Horsepower"}
,
{"question":"How many mother sauces are there in classical French cuisine?","answer":"Five"}
,
{"question":"In what country would you find the temple complex Angkor Wat?","answer":"Cambodia"}
,
{"question":"What is the meaning of the French expression \"c'est la vie\"?","answer":"That's life"}
,
{"question":"The Hoover Dam in the United States is built on what river?","answer":"The Colorado River"}
,
{"question":"What is the largest ocean on planet Earth?","answer":"Pacific Ocean"}
,
{"question":"Which of the Beatles is barefoot on the Abby Road album cover?","answer":"Paul McCartney"}
,
{"question":"Orphan Black is a sci-fi television series filmed in which country?","answer":"Canada"}
,
{"question":"In Disney's \"The Little Mermaid\" what is the name of the human that Ariel falls in love with?","answer":"Prince Eric"}
,
{"question":"What is the largest species of terrestrial crab in the world?","answer":"The coconut crab (Birgus latro)"}
,
{"question":"Which American inventor is generally given credit for the invention of the lightning rod?","answer":"Benjamin Franklin"}
,
{"question":"Which actress plays the female lead in the American crime thriller television series \"The Blacklist\"?","answer":"Megan Boone"}
,
{"question":"The original Starbucks was established in 1971 in what U.S. city?","answer":"Seattle, Washington"}
,
{"question":"Carved stone human figures with large heads, known as Moai, can be found on what Poloneysian island?","answer":"Easter Island (Rapa Nui)"}
,
{"question":"Which American author wrote the novel \"The Great Gatsby\", published in 1922?","answer":"F. Scott Fitzgerald"}
,
{"question":"What do the letters in the acronym CD-ROM stand for?","answer":"Compact Disk Read Only Memory"}
,
{"question":"Titan, Enceladus, Mimas & Iapetus are just some of the moons orbiting which planet?","answer":"Saturn"}
,
{"question":"Jimmy Carter was the first U.S. president born in a what?","answer":"Hospital"}
,
{"question":"In welding terminology, what do the letters MIG stand for?","answer":"Metal Inert Gas"}
,
{"question":"What is the name for a male bee that comes from an unfertilized egg?","answer":"Drone"}
,
{"question":"Which major American airline is named after a greek letter?","answer":"Delta"}
,
{"question":"In China, what number is considered unlucky because its pronunciation is similar to that for the word \"death\"?","answer":"Four (四,sì)"}
,
{"question":"The United States Constitution replaced what other document on March 4, 1789?","answer":"The Articles of Confederation"}
,
{"question":"Which actress played the genie in the American comedy sitcom \"I Dream of Jeannie\"?","answer":"Barbara Eden"}
,
{"question":"What is the highest enlisted rank a soldier can hold in the United States Army?","answer":"Sergeant Major of the Army"}
,
{"question":"What is the name of the official currency of Costa Rica?","answer":"Costa Rican Colón"}
,
{"question":"What is the name of the longest mountain range in North America?","answer":"Rocky Mountains"}
,
{"question":"When found on a beer bottle, what does the acronym IPA stand for?","answer":"India Pale Ale"}
,
{"question":"In 1867 the United States purchased Alaska from what country?","answer":"Russia"}
,
{"question":"What do the letters \"PT\" stand for in the name of Chrysler's family car, the PT Cruiser?","answer":"Personal Transport"}
,
{"question":"K-pop is a genre of music that originated in what country?","answer":"South Korea"}
,
{"question":"In 1975 an engineer created the first electronic camera while working for what company?","answer":"Kodak"}
,
{"question":"In humans, what is the only internal organ capable of regenerating lost tissue?","answer":"The Liver"}
,
{"question":"Ruling for 64 years, which Queen was the longest-reigning British monarch before Queen Elizabeth II?","answer":"Queen Victoria"}
,
{"question":"In which South American country would you find the ancient Incan citadel Machu Picchu?","answer":"Peru"}
,
{"question":"Who wrote the young adult vampire-romance novel \"Twilight\"?","answer":"Stephenie Meyer"}
,
{"question":"What is the name of the animated science fiction comedy-drama film released in 2002 about a Hawaiin girl and her unusual pet?","answer":"Lilo & Stitch"}
,
{"question":"The first McDonald's restaurant openend in which U.S. state?","answer":"California"}
,
{"question":"What is the color of the five stars found on the flag of China?","answer":"Yellow"}
,
{"question":"What do the letters \"ZIP\" stand for in the United States postal code?","answer":"Zone Improvement Plan"}
,
{"question":"Cynophobia is the fear of what kind of animal?","answer":"Dogs"}
,
{"question":"The first generation of the Chevrolet Corvette was introduced in what year?","answer":"1953"}
,
{"question":"In movie ratings what do the letters PG stand for?","answer":"Parental Guidance"}
,
{"question":"Nintendo is a consumer electronics and video game company founded in what country?","answer":"Japan"}
,
{"question":"What football team had the biggest scoring comeback in the history of the Super Bowl?","answer":"Patriots (Super Bowl LI)"}
,
{"question":"What does the military acronym HALO stand for?","answer":"High Altitude-Low Opening"}
,
{"question":"In the Star Wars universe, who is Luke Skywalker's mother?","answer":"Padmé Amidala"}
,
{"question":"The inventor Nikola Tesla was born on July 10th 1856 in what modern day country?","answer":"Croatia"}
,
{"question":"In the \"Lord of the Rings\" film series which actor plays the character of Saruman?","answer":"Christopher Lee"}
,
{"question":"San Marino is a microstate in Europe completely surrounded by what country?","answer":"Italy"}
,
{"question":"Who is the longest reigning heavyweight boxing champion with 25 successful defenses?","answer":"Joe Louis"}
,
{"question":"In a photo editing program, what do the letters RGB stand for?","answer":"Red, Green & Blue"}
,
{"question":"The reaction where two atoms of hydrogen combine to form an atom of helium is called what?","answer":"Fusion"}
,
{"question":"Who is credited with suggesting the word \"hello\" be used when answering the telephone?","answer":"Thomas Edison"}
,
{"question":"Which British author wrote the popular children's novel \"James and the Giant Peach\"?","answer":"Roald Dahl"}
,
{"question":"What is the Easternmost point on the North American continent?","answer":"Cape Spear, Newfoundland, Canada"}
,
{"question":"Award winning Latina pop artist Shakira was born in raised in what Country?","answer":"Colombia"}
,
{"question":"\"Torchwood\" is an anagram and spin-off of what popular British sci-fi series?","answer":"Doctor Who"}
,
{"question":"Roquefort is a French blue cheese made from the milk of what animal?","answer":"Sheep"}
,
{"question":"The St. Lawrence River forms part of the border between which two countries?","answer":"The United States & Canada"}
,
{"question":"A Grammy is an award to recognize outstanding achievement in what industry?","answer":"Music"}
,
{"question":"What were the six original Hockey teams of the National Hockey League?","answer":"Boston Bruins, Chicago Black Hawks, Detroit Red Wings, Montreal Canadiens, New York Rangers, and Toronto Maple Leafs"}
,
{"question":"The term wake, kettle, or committee refers to a group of what bird?","answer":"Vulture"}
,
{"question":"Ceres is a dwarf planet that lies between the orbits of which two planets in our solar system?","answer":"Mars & Jupiter"}
,
{"question":"What battle was fought on June 18th, 1815 in present-day Belgium?","answer":"The Battle of Waterloo"}
,
{"question":"Star Trek - The Next Generation originally aired in what year?","answer":"1987"}
,
{"question":"Spaceship Earth is the icon for what amusement park that features technological innovation and international culture?","answer":"Epcot"}
,
{"question":"What is the name for trees that never lose their leaves?","answer":"Evergreen"}
,
{"question":"Formerly known as Bedloe's Island, what is the current name of the island where the Statue of Liberty is located?","answer":"Liberty Island"}
,
{"question":"Approximately 2% of all people have what eye color?","answer":"Green"}
,
{"question":"What fast food franchise has the most worldwide locations?","answer":"Subway"}
,
{"question":"What is the name of the phenomenon when the magnetosphere in the Northern Hemisphere is disturbed by the solar wind resulting in a natural light display?","answer":"Aurora Borealis (Northern Lights)"}
,
{"question":"HTML and CSS are computer languages used to create what?","answer":"Websites"}
,
{"question":"\"Granny Smith\" is a popular type of which fruit?","answer":"Apple"}
,
{"question":"Jean-Paul Sartre and Le Duc Tho both declined to accept what famous international award?","answer":"The Nobel Prize"}
,
{"question":"Who was vice president of the United States when Lincoln was assassinated?","answer":"Andrew Johnson"}
,
{"question":"How many pairs of chromosomes are in found in the average human?","answer":"Twenty-three"}
,
{"question":"\"Stairway to Heavan\" a song by English rock band Led Zeppelin was originally released on which of their albums?","answer":"Their untitled fourth studio album commonly referred to as \"Led Zeppelin IV\"."}
,
{"question":"The first human-made object to land on the moon was launched by what country?","answer":"The Soviet Union"}
,
{"question":"War and Peace, originally published in 1869, is a novel written by which Russian author?","answer":"Leo Tolstoy"}
,
{"question":"What U.S. national park, located in the Northwest corner of Montana, has the nickname \"Crown of the Continent\"?","answer":"Glacier National Park"}
,
{"question":"Sardinia, the second largest island in the Mediterranean Sea, is an autonomous region of what country?","answer":"Italy"}
,
{"question":"Who was the Prime Minister of Italy during WWII?","answer":"Benito Amilcare Andrea Mussolin"}
,
{"question":"What American punk rock band released their best selling album \"Dookie\" in 1994?","answer":"Green Day"}
,
{"question":"Beirut is the capital and largest city of what country?","answer":"Lebanon"}
,
{"question":"Barry Bonds currently holds the Major League Baseball home run record with how many home runs?","answer":"762"}
,
{"question":"Dijon mustand originated in the city of Dijon, located in what country?","answer":"France"}
,
{"question":"The first movie of the Fast and Furious franchise was released in what year?","answer":"2001"}
,
{"question":"The Grand Canyon is located in which U.S. state?","answer":"Arizona"}
,
{"question":"In music, the space between one musical pitch and another with double its frequency is called what?","answer":"An octave"}
,
{"question":"In the children's books about a 25 foot tall red dog, what is the name of the dog?","answer":"Clifford"}
,
{"question":"Located in Northwestern Turkey, which strait separates Europe and Asia?","answer":"Bosphorus Strait"}
,
{"question":"Who is the oldest person to be elected to the office of President of the United States?","answer":"Donald Trump"}
,
{"question":"The atmospheric temperature at which water vapor begins to condense and form dew, is called what?","answer":"Dew Point"}
,
{"question":"In 1783, the first free flight of a hot air balloon carrying a human occured in what city?","answer":"Paris, France"}
,
{"question":"American singer-songwriter Johny Cash passed away in what year?","answer":"2003"}
,
{"question":"What is the longest running U.S. primetime television show of all time?","answer":"The Simpsons"}
,
{"question":"In most modern vehicles, the carburator has been replace with what?","answer":"Fuel Injection"}
,
{"question":"\"Being and Time\" is an ontological treatise written by which German philosopher?","answer":"Martin Heidegger"}
,
{"question":"In the 2016 American fantasy adventure film, \"The Jungle Book\", what is the name of the orphaned human boy?","answer":"Mowgli"}
,
{"question":"Who is the Canadian singer-songwriter best known for her hit song, \"Call Me Maybe\"?","answer":"Carly Rae Jepsen"}
,
{"question":"In fluid dynamics, what is the term for the highest attainable speed an object can reach as it falls?","answer":"Terminal Velocity"}
,
{"question":"South Africa completely surrounds which other African nation?","answer":"Lesotho"}
,
{"question":"Europe is separated from Asia by which mountain range?","answer":"Ural Mountains"}
,
{"question":"In the movie \"The Wizard of Oz\", what did the Scarecrow want from the wizard?","answer":"A brain"}
,
{"question":"In what year did McDonald's start serving breakfast with the introduction of the Egg McMuffin?","answer":"1972"}
,
{"question":"Founded in 1607, what is considered to be the first permanent English settlement in the New World?","answer":"Jamestown, Virginia"}
,
{"question":"Which of the traditional five senses are dolphins believed not to possess?","answer":"Smell"}
,
{"question":"Which actress played identical twins in the 1998 movie remake of The Parent Trap?","answer":"Lindsay Lohan"}
,
{"question":"What is the largest country in North America?","answer":"Canada"}
,
{"question":"A flamboyance is a group of what animal?","answer":"Flamingos"}
,
{"question":"What is professional wrestler John Cena's famous catchphrase?","answer":"You can't see me!"}
,
{"question":"The Chihuahua is a breed of dog believed to originate from what country?","answer":"Mexico"}
,
{"question":"The use of chopsticks originated in what country?","answer":"China"}
,
{"question":"What is a group of whales called?","answer":"A pod"}
,
{"question":"The oldest parliament in the world belongs to what country?","answer":"Iceland"}
,
{"question":"Pupusas, handmade thick stuffed corn tortillas, are a traditional dish from what country?","answer":"El Salvador"}
,
{"question":"Which tennis player has won the most men's Grand Slam titles?","answer":"Roger Federer"}
,
{"question":"Which Irish author wrote the avant-garde comic fiction,\"Finnegans Wake\"?","answer":"James Joyce"}
,
{"question":"What famous dictator was assasinated on the Ides of March?","answer":"Julius Caesar"}
,
{"question":"What is the name of Atlanta's major league baseball team?","answer":"Atlanta Braves"}
,
{"question":"What was the name of the U.S. mail service, started in 1860, that used horses and riders?","answer":"Pony Express"}
,
{"question":"What does the Statue of Liberty hold in her right hand?","answer":"A torch"}
,
{"question":"In which 1993 thriller does the protagonist violently lose his cool when a fast food restaurant will not let him order from the breakfast menu?","answer":"Falling Down"}
,
{"question":"Who is the only athlete ever to play in a Super Bowl and a World Series?","answer":"Deion Sanders"}
,
{"question":"The term \"déjà vu\" comes from what language?","answer":"French"}
,
{"question":"What is the colloquial term for a rotating tray often often placed on a table to aid in distributing food?","answer":"Lazy Susan"}
,
{"question":"In hockey, how many players from each team are allowed to be on the ice at the same time?","answer":"Six"}
,
{"question":"The Great Pyramid of Giza is located in what Egyptian city?","answer":"Giza"}
,
{"question":"According to NBA rules how long does a player have after catching the ball to shoot a free throw?","answer":"10 seconds"}
,
{"question":"Which of the great lakes does not share a border with Canada?","answer":"Lake Michigan"}
,
{"question":"The first person shooter video game Doom was first released in what year?","answer":"1993"}
,
{"question":"What is the real name of the former wrestler turned actor who went by the ring name \"The Rock\"?","answer":"Dwayne Douglas Johnson"}
,
{"question":"What is the proper term for a group of parrots?","answer":"Pandemonium"}
,
{"question":"Who is the lead singer for the American rock band Pearl Jam?","answer":"Eddie Vedder"}
,
{"question":"Who wrote the Pledge of Allegiance of the United States?","answer":"Francis Bellamy"}
,
{"question":"What is the name of the 1978 movie, starring Brad Davis, about an American college student who is sent to a Turkish prison for attempting to smuggle hashish out of Turkey?","answer":"Midnight Express"}
,
{"question":"What luxury British automobile brand was purchased by by Tata motors in 2008?","answer":"Jaguar"}
,
{"question":"What popular soda beverage was originally developed as a mixer for whiskey?","answer":"Mountain Dew"}
,
{"question":"Which country won the 2012 UEFA European Championship?","answer":"Spain"}
,
{"question":"What is the name of the actress who plays Hermione Granger in the Harry Potter series of films?","answer":"Emma Watson"}
,
{"question":"How many furlongs are there in one mile?","answer":"Eight"}
,
{"question":"What was the name of the U.S. research and development project to create nuclear weapons in WWII?","answer":"Manhattan Project"}
,
{"question":"What is the national language of India?","answer":"Hindi"}
,
{"question":"What was the name of Seattle grundge band Nirvana's first album, released in 1989?","answer":"Bleach"}
,
{"question":"In the Disney movie \"Beauty and the Beast\", what is the name of Gaston's bumbling sidekick?","answer":"LeFou"}
,
{"question":"The ancient Greek statue Ahprodite of Milos, better known as Venus de Milo, is currently on display in what museum?","answer":"The Louvre in Paris, France"}
,
{"question":"What does the acronym \"lol\" stand for when used in phone texts and on the internet?","answer":"Laugh out loud"}
,
{"question":"What is the largest island in the Caribbean Sea?","answer":"Cuba"}
,
{"question":"What is the unit of length that is approximately 3.26 light-years?","answer":"Parsec"}
,
{"question":"What animal has the largest ears?","answer":"African elephant"}
,
{"question":"Who came up with the theories of General and Special relativity?","answer":"Albert Einstein"}
,
{"question":"In sports, what does the acronym MVP stand for?","answer":"Most valuable player"}
,
{"question":"What is the national animal of Scotland?","answer":"Unicorn"}
,
{"question":"Which is the most abundant metal in the earth's crust?","answer":"Aluminum"}
,
{"question":"What was the name of the first U.S. space station?","answer":"Skylab"}
,
{"question":"In what year was Alfred Hitchcock's psychological thriller \"Psycho\" released?","answer":"1960"}
,
{"question":"What is the second most abundant element in the earth's atmosphere?","answer":"Oxygen"}
,
{"question":"In the United States, where can alligators and crocodiles be found together in the wild?","answer":"South Florida"}
,
{"question":"What are the four houses at Hogwarts School of Witchcraft and Wizardry?","answer":"Gryffindor, Ravenclaw, Hufflepuff, & Slytherin"}
,
{"question":"What was the name of the kleptomaniac monkey in the Disney movie \"Aladdin\"?","answer":"Abu"}
,
{"question":"What was the original flavor of the filling in Twinkies?","answer":"Banana cream"}
,
{"question":"What is the largest 3-digit prime number?","answer":"997"}
,
{"question":"Which psychologist investigated obedience using electric shocks?","answer":"Stanley Milgram"}
,
{"question":"What vitamin is produced when a person is exposed to sunlight?","answer":"Vitamin D"}
,
{"question":"What are the names of the three fairies in the Disney classic \"Sleeping Beauty\"?","answer":"Flora, Fauna and Merryweather"}
,
{"question":"What is the name for a protein that acts as a biological catalyst?","answer":"Enzyme"}
,
{"question":"What is Michael J. Fox's middle name?","answer":"Andrew"}
,
{"question":"Sauerkraut is made from what finely cut vegetable?","answer":"Cabbage"}
,
{"question":"Who is the author of the novella \"The Metamorphosis\", first published in 1915?","answer":"Franz Kafka"}
,
{"question":"Who played James Bond in the 1969 film \"On Her Majesty's Secret Service\"?","answer":"George Robert Lazenby"}
,
{"question":"Quasimodo is a fictional character from what novel?","answer":"The Hunchback of Notre-Dam"}
,
{"question":"Keiko is the name of a whale that appeared in what 1993 American family drama film?","answer":"Free Willy"}
,
{"question":"The Simpsons first debuted as a short in what American variety television show?","answer":"The Tracey Ullman Show"}
,
{"question":"Which planet in our solar system has the most oxygen?","answer":"Earth"}
,
{"question":"Which team did the Chicago Cubs play in the 1945 World Series?","answer":"Detroit Tigers"}
,
{"question":"In what year was Alfred Hitchcock's psychological thriller \"Psycho\" released?","answer":"1960"}
,
{"question":"What is the second most abundant element in the earth's atmosphere?","answer":"Oxygen"}
,
{"question":"In the United States, where can alligators and crocodiles be found together in the wild?","answer":"South Florida"}
,
{"question":"What are the four houses at Hogwarts School of Witchcraft and Wizardry?","answer":"Gryffindor, Ravenclaw, Hufflepuff, & Slytherin"}
,
{"question":"What was the name of the kleptomaniac monkey in the Disney movie \"Aladdin\"?","answer":"Abu"}
,
{"question":"What was the original flavor of the filling in Twinkies?","answer":"Banana cream"}
,
{"question":"What is the largest 3-digit prime number?","answer":"997"}
,
{"question":"What is Michael J. Fox's middle name?","answer":"Andrew"}
,
{"question":"Sauerkraut is made from what finely cut vegetable?","answer":"Cabbage"}
,
{"question":"Who is the author of the novella \"The Metamorphosis\", first published in 1915?","answer":"Franz Kafka"}
,
{"question":"Who played James Bond in the 1969 film \"On Her Majesty's Secret Service\"?","answer":"George Robert Lazenby"}
,
{"question":"Quasimodo is a fictional character from what novel?","answer":"The Hunchback of Notre-Dam"}
,
{"question":"Keiko is the name of a whale that appeared in what 1993 American family drama film?","answer":"Free Willy"}
,
{"question":"Which planet in our solar system has the most oxygen?","answer":"Earth"}
,
{"question":"Which team did the Chicago Cubs play in the 1945 World Series?","answer":"Detroit Tigers"}
,
{"question":"In a website browser address bar what does \"www\" stand for?","answer":"World Wide Web"}
,
{"question":"Long Island is a part of which US state?","answer":"New York"}
,
{"question":"According to Guiness World Records, which author has the most published works?","answer":"L. Ron Hubbard"}
,
{"question":"Each of a classic Rubik's Cube six faces is covered by how many stickers?","answer":"Nine"}
,
{"question":"The European Organization for Nuclear Research is known by what four letter acronym?","answer":"CERN"}
,
{"question":"Barack Obama was first elected president of the United States in what year?","answer":"2008"}
,
{"question":"Brazil was once a colony of which European country?","answer":"Portugal"}
,
{"question":"The final link of the first transcontinental railroad across the United States was completed in which state?","answer":"Utah"}
,
{"question":"What American singer-songwriter wrote and first recorded the song \"Blue Suede Shoes\" in 1955?","answer":"Carl Perkins"}
,
{"question":"Who painted a late 15th-century mural known as the Last Supper?","answer":"Leonardo da Vinci"}
,
{"question":"What is the melting point of ice in Fahrenheit?","answer":"32°F"}
,
{"question":"What country was host to the 1930 inaugural FIFA Football World Cup?","answer":"Uruguay"}
,
{"question":"Who played the title character in the teen sitcom musical comedy \"Hannah Montana\"?","answer":"Miley Cyrus"}
,
{"question":"The cooking technique that involves submerging food in a liquid at a relatively low temperature is called what?","answer":"Poaching"}
,
{"question":"What is the most popular board game of all time?","answer":"Chess"}
,
{"question":"Yerevan, one of the world's oldest continuously inhabited cities, is the capital of what country?","answer":"Armenia"}
,
{"question":"Polar bears feed mainly on what animal?","answer":"Seals"}
,
{"question":"What sunglasses did Tom Cruise wear in the 1986 movie \"Top Gun\"?","answer":"Ray Ban Aviator (RB 3025)"}
,
{"question":"Singer-songwriter George Michael, famous for such hits as \"Faith\" and \"Father Figure\", passed away in what year?","answer":"2016"}
,
{"question":"What was the first commercial product that had a Barcode?","answer":"Wrigley’s Juicy Fruit Gum"}
,
{"question":"Who wrote and recorded the one hit wonder \"Spirit in the Sky\" released in late 1969?","answer":"Norman Greenbaum"}
,
{"question":"What are the names of the two actors whose characters get stuck traveling together in the movie \"Trains Planes & Automobiles\"?","answer":"Steve Martin & John Candy"}
,
{"question":"Which branch of physics is devoted to the study of heat and related phenomen?","answer":"Thermodynamics"}
,
{"question":"Hopalong Cassidy is a fictional cowboy hero, what was the name of his horse?","answer":"Topper"}
,
{"question":"What are the seven base units of measurement in the metric system?","answer":"The ampere, the candela, the kelvin, the kilogram, the meter, the mole and the second"}
,
{"question":"How many super bowls have the Denver Broncos won?","answer":"Three"}
,
{"question":"What is the name of the actress who played the Unsinkable Molly Brown in the 1997 movie Titanic?","answer":"Kathy Bates"}
,
{"question":"What is the capital of Iceland?","answer":"Reykjavik"}
,
{"question":"What is a group of rhinoceros called?","answer":"A \"crash\""}
,
{"question":"The Alaskan Malamute is a type of what?","answer":"Dog"}
,
{"question":"Rod Serling created what famous science fiction television show?","answer":"The Twilight Zone"}
,
{"question":"The Stanley Cup is a championship trophy awarded annually to the playoff winner in what sport?","answer":"Hockey"}
,
{"question":"What does the acronym \"NASA\" stand for?","answer":"National Aeronautics and Space Administration"}
,
{"question":"What is the largest lake in Africa?","answer":"Lake Victoria"}
,
{"question":"What did the letters of the former communist country U.S.S.R. stand for?","answer":"Union of Soviet Socialist Republics"}
,
{"question":"What is the main dialect of Chinese spoken in Hong Kong by the majority of the locals?","answer":"Cantonese"}
,
{"question":"What is the name of the deepest known location in the Earth's oceans?","answer":"Challenger Deep"}
,
{"question":"What is the tallest building in New York?","answer":"One World Trade Center"}
,
{"question":"What was the full name of British novelist C. S. Lewis?","answer":"Clive Staples Lewis"}
,
{"question":"What sport does Cristiano Ronaldo play?","answer":"Soccer (football)"}
,
{"question":"Which Patriot leader organized the Boston Tea Party in 1773?","answer":"Samuel Adams"}
,
{"question":"In what type of restaurant would you typically find the condiment wasabi?","answer":"Japanese"}
,
{"question":"What was the first ever series to air on the Disney Channel?","answer":"Good Morning, Mickey"}
,
{"question":"What was the highest selling album of the 1980s in the United States?","answer":"Thriller by Michael Jackson"}
,
{"question":"How many planets in our solar system have moons?","answer":"Six"}
,
{"question":"Canada's highest mountain is located in which province or territory?","answer":"Yukon"}
,
{"question":"What layer of the atmosphere lies between the troposphere and mesosphere?","answer":"Stratosphere"}
,
{"question":"In what year did Fidel Castro die?","answer":"2016"}
,
{"question":"How many times zones are in Canada?","answer":"Six"}
,
{"question":"What does the \"B\" stand for in Lyndon B. Johnson?","answer":"Baines"}
,
{"question":"In what year did Nintendo release its first game console in North America?","answer":"1985"}
,
{"question":"In what year did India gain its independence from Britain?","answer":"1947"}
,
{"question":"How do you say \"I love you\" in Italian?","answer":"Ti amo"}
,
{"question":"What is a baby turkey called?","answer":"Poult or chick"}
,
{"question":"In what year was the \"Perfect 10\" scoring system in gymnastics abandoned?","answer":"2006"}
,
{"question":"Who was the mayor of New York City during the September 11 attacks in 2001?","answer":"Rudy Giuliani"}
,
{"question":"Which planet is farthest from the sun?","answer":"Neptune"}
,
{"question":"What musical instrument did Sherlock Holmes play?","answer":"Violin"}
,
{"question":"Natural pearls are found in what sea creature?","answer":"Oyster"}
,
{"question":"\"Hallelujah\" is a song written by which Canadian recording artist?","answer":"Leonard Cohen"}
,
{"question":"Which NFL Quarterback has been to the most Super Bowls?","answer":"Tom Brady"}
,
{"question":"FARC is the acronym for a guerrilla movement originating in which country?","answer":"Colombia"}
,
{"question":"The United Kingdom's withdrawal from the European Union is commonly known as what?","answer":"Brexit"}
,
{"question":"The Commonwealth of the Bahamas gained independence in 1973 from what country?","answer":"United Kingdom"}
,
{"question":"What was the Roman name for the goddess Hecate?","answer":"Trivia"}
,
{"question":"\"All Shook Up\" is a song that topped the U.S. Billboard Hot 100 on April 13, 1957. Who was the singer?","answer":"Elvis Presley"}
,
{"question":"What do the letters of the popular fast food chain KFC stand for?","answer":"Kentucky Fried Chicken"}
,
{"question":"Which Christopher Columbus ship ran aground on his first voyage?","answer":"La Santa Maria"}
,
{"question":"What planet in our solar system has the most gravity?","answer":"Jupiter"}
,
{"question":"Which ocean trench is the deepest?","answer":"Mariana Trench or Marianas Trench"}
,
{"question":"What is the capital city of Australia?","answer":"Canberra"}
,
{"question":"Cogito ergo sum, \"I think, therefore I am\", is a Latin phrase by which philospher?","answer":"René Descartes"}
,
{"question":"The Passenger Pigeon, now extinct, was endemic to which continent?","answer":"North America"}
,
{"question":"What was the title of Kayne West's debut album release in 2004?","answer":"The College Dropout"}
,
{"question":"Portugal is bordered by what other country?","answer":"Spain"}
,
{"question":"Who won the Nobel Prize for Literature in 2016?","answer":"Bob Dylan"}
,
{"question":"Who assassinated President Abraham Lincoln?","answer":"John Wilkes Booth"}
,
{"question":"Steve Jobs, Steve Wozniak, and Ronald Wayne founded what company in 1976?","answer":"Apple Computer, Inc."}
,
{"question":"The Giza Plateau can be found in what country?","answer":"Egypt"}
,
{"question":"What is the common name for stone consisting of the minerals jadeite or nephrite?","answer":"Jade"}
,
{"question":"What is the largest internal organ of the human body?","answer":"Liver"}
,
{"question":"Mr. Pibb was a soft drink created by the Coca-Cola Company to compete with what other soft drink?","answer":"Dr Pepper"}
,
{"question":"The Yangtze River is entirely located in which country?","answer":"The People's Republic of China"}
,
{"question":"What is the highest score possible in 10 pin bowling?","answer":"300"}
,
{"question":"Who was the first Tudor monarch in England?","answer":"Henry VII"}
,
{"question":"Which five-times Grand Slam tennis champion tested postive for a banned substance at the 2016 Australian Open?","answer":"Maria Sharapova"}
,
{"question":"Curiosity is a car-sized rover that was launched by NASA in 2011 to explore which planet?","answer":"Mars"}
,
{"question":"The Kingdom of Joseon was founded in 1392 in what country?","answer":"Korea"}
,
{"question":"What is the fastest fish in the Ocean?","answer":"Sailfish"}
,
{"question":"The Spanish Civil War began in what year?","answer":"1936"}
,
{"question":"What is name of the scale used to measure the spicy heat of peppers?","answer":"Scoville scale"}
,
{"question":"Who came up with the three laws of motion?","answer":"Sir Isaac Newton"}
,
{"question":"What was the name of Taylor Swift's first album?","answer":"Taylor Swift"}
,
{"question":"Manga are a type of comics from what country?","answer":"Japan"}
,
{"question":"What song by Michael Jackson contains the lyrics \"Annie are you OK?\"","answer":"Smooth Criminal"}
,
{"question":"How many U.S. presidents were only children?","answer":"None"}
,
{"question":"What is the regulation height for a basketball hoop?","answer":"10 feet (3.048 m)"}
,
{"question":"Which animal has the most legs?","answer":"Millipede"}
,
{"question":"How many letters are in the modern English alphabet?","answer":"26"}
,
{"question":"In which city did Rosa Parks famously refuse to give up her seat on the bus?","answer":"Montgomery Alabama"}
,
{"question":"Pho is a popular noodle soup from what country?","answer":"Vietnam"}
,
{"question":"Who designed and built the Pascaline?","answer":"Blaise Pascal"}
,
{"question":"Madagascar is an island located of the southeast coast of what continent?","answer":"Africa"}
,
{"question":"What is the medical term for bad breath?","answer":"Halitosis"}
,
{"question":"Cruella de Vil is a character who appeared in what novel by Dodie Smith?","answer":"The Hundred and One Dalmatians"}
,
{"question":"What was the name of The Lone Ranger's horse that he saved from an enraged buffalo?","answer":"Silver"}
,
{"question":"The Pascaline, invented by Blaise Pascal in the early 17th century, was a mechanical type of what device?","answer":"Calculator"}
,
{"question":"Lake Tahoe straddles the border between which two U.S. states?","answer":"California & Nevada"}
,
{"question":"How do you say \"hello\" in Swedish?","answer":"Hej"}
,
{"question":"The Kangaroo Hoppet is a long distance cross-country skiing race that is held in which county?","answer":"Australia"}
,
{"question":"Frankenmuth, a U.S. city nicknamed \"Little Bavaria\", is located in what state?","answer":"Michigan"}
,
{"question":"In what year was the Declaration of Independence created?","answer":"1776"}
,
{"question":"What year was Facebook founded?","answer":"2004"}
,
{"question":"What are baby beavers called?","answer":"Kittens or Kits"}
,
{"question":"What is the fastest land snake in the world?","answer":"Black Mamba"}
,
{"question":"What is the scientific name of the common potato?","answer":"Solanum tuberosum L."}
,
{"question":"How many elevators does the Empire State Building have?","answer":"73"}
,
{"question":"Callisto is the name of a moon orbiting what planet in our solar system?","answer":"Jupiter"}
,
{"question":"What was the name of Michael Jackson's first solo album as an adult?","answer":"Off The Wall"}
,
{"question":"Nicholas II, the last Tsar of Russia was said to have been close friends with a mystical faith healer known by what name?","answer":"Grigori Rasputin"}
,
{"question":"Penicillin is used to fight what type of infections?","answer":"Bacterial"}
,
{"question":"Which two elements on the periodic table are liquids at room temperature?","answer":"Mercury and Bromine"}
,
{"question":"In what country would you find Mount Kilimanjaro?","answer":"Tanzania"}
,
{"question":"While walking through the woods in 1941, George de Mestral was inspred by the burrs that clung to his pants to create what product?","answer":"Velcro"}
,
{"question":"Fe is the chemical symbol for what element?","answer":"Iron"}
,
{"question":"What is the capital city of the Philippines?","answer":"Manila"}
,
{"question":"Red Vines is a popular brand of what type of candy?","answer":"Red licorice"}
,
{"question":"Who was the first Roman Catholic to be Vice President of the United States of America?","answer":"Joe Biden"}
,
{"question":"John Montagu, the man credited with inventing the sandwich, held what noble title?","answer":"Earl of Sandwich"}
,
{"question":"Cubic zirconia is a synthesized material often used in place of what precious stone?","answer":"Diamond"}
,
{"question":"Who was the first First Lady to be elected to public office?","answer":"Hillary Rodham Clinton"}
,
{"question":"According to physics, what are the four fundamental forces in nature?","answer":"Strong Force, Electromagnetic Force, Weak Force, Gravitational Force"}
,
{"question":"Which animal was incorrectly rumored to bury its head in the sand when frightened?","answer":"Ostrich"}
,
{"question":"The filament in an incandescent light bulb is made of what element?","answer":"Tungsten"}
,
{"question":"Which is the closest galaxy to the milky way?","answer":"Andromeda galaxy, about 2.5 million light years away"}
,
{"question":"What is the capital of the Republic of Ireland?","answer":"Dublin"}
,
{"question":"Au is the symbol for for what chemical element?","answer":"Gold"}
,
{"question":"The taste that allows us to taste savory foods is called what?","answer":"Umami"}
,
{"question":"The paperboard \"Chinese takeout\" box was invented in what country?","answer":"The United States"}
,
{"question":"Who declined the 1964 Nobel Prize for literature?","answer":"Jean-Paul Sartre"}
,
{"question":"In computer science, what does \"GUI\" stand for?","answer":"Graphical user interface"}
,
{"question":"Shaquille Rashaun O'Neal retired in 2011 from what sport?","answer":"Basketball"}
,
{"question":"In what city was Ludwig van Beethoven born?","answer":"Bonn, Electorate of Cologne"}
,
{"question":"Abraham Lincoln was assassinated in what year?","answer":"1865"}
,
{"question":"Geelong is a port city located in what country?","answer":"Australia"}
,
{"question":"Robin Williams won an Academy Award for best supporting actor in which 1997 film about a South Boston janitor?","answer":"Good Will Hunting"}
,
{"question":"In database programming, SQL is an acronym for what?","answer":"Structured Query Language"}
,
{"question":"How do you say hello in Mandarin Chinese?","answer":"Ni Hao"}
,
{"question":"The Grand Slam tournaments are the four most import annual events in which two sports?","answer":"Tennis & Golf"}
,
{"question":"The State of Israel was founded in what year?","answer":"1948"}
,
{"question":"Schrödinger's cat is a thought experiment dealing with which type of mechanics?","answer":"Quantum Mechanics"}
,
{"question":"In the late 1890s, Bayer marketed a cough, cold & pain remedy that contained what now illegal drug?","answer":"Heroin"}
,
{"question":"What is the name of Mickey Mouse´s dog?","answer":"Pluto"}
,
{"question":"The famous Actress Winona Ryder had what last name at birth?","answer":"Horowitz"}
,
{"question":"What is the smallest and most endagered species of sloth?","answer":"The pygmy three-toed sloth (Bradypus pygmaeus)"}
,
{"question":"In Russia, a woman's last name usually ends in what letter?","answer":"A"}
,
{"question":"The Black Forest is located in what European country?","answer":"Germany"}
,
{"question":"The assasination that is said to have lead to World War I, occured in what city?","answer":"Sarajevo"}
,
{"question":"Tom Hanks played \"Captain Miller\" in what legendary World War II movie?","answer":"Saving Private Ryan"}
,
{"question":"Who was the first NASA austronaut to visit space twice?","answer":"Gus Grissom"}
,
{"question":"In what year did Paul McCartney announce he was quitting the Beatles?","answer":"1970"}
,
{"question":"El Clásico is the name given to football (soccer) matches between which two teams?","answer":"Real Madrid and FC Barcelona"}
,
{"question":"BB-8 is an astromech droid from what film franchise?","answer":"Star Wars"}
,
{"question":"What is the third most abundant gas in Earth's atmosphere?","answer":"Argon"}
,
{"question":"Where was the very first Hard Rock Cafe opened?","answer":"Piccadilly, London"}
,
{"question":"What is the capital city of Croatia?","answer":"Zagreb"}
,
{"question":"Porsche is a brand of car that originated in what country?","answer":"Germany"}
,
{"question":"In what year was Nelson Mandela released from prison?","answer":"1990"}
,
{"question":"Ireland suffered the Great Famine beginning in 1845 due to the collapse of what crop?","answer":"Potato"}
,
{"question":"What type of bridge is the Golden Gate Bridge?","answer":"Suspension"}
,
{"question":"What is the first book of the bible?","answer":"Genesis"}
,
{"question":"Sinterklaas is the Dutch version of what mythical figure?","answer":"Santa Claus (Saint Nicholas)"}
,
{"question":"Magarine is sold as a replacement for what?","answer":"Butter"}
,
{"question":"The original Ghostbusters movie was released in June of what year?","answer":"1984"}
,
{"question":"Which book was famously rejected by 12 publishers before finally being accepted by Bloomsbury?","answer":"Harry Potter and The Philosopher's Stone"}
,
{"question":"NASCAR is an acronym for what family-owned and operated business?","answer":"The National Association for Stock Car Auto Racing"}
,
{"question":"Which hockey player has won the most Stanley Cups with 11 wins?","answer":"Henri Richard"}
,
{"question":"Which city is located both in Asia and Europe?","answer":"Istanbul"}
,
{"question":"Chimichurri is a green sauce that originated in what country?","answer":"Argentina"}
,
{"question":"Who is considered the father of psychoanalysis?","answer":"Sigmund Freud"}
,
{"question":"Who was the author of \"The Amityville Horror\" published in 1977?","answer":"Jay Anson"}
,
{"question":"What city is the capital of India?","answer":"New Delhi"}
,
{"question":"Our solar system is located in what galaxy?","answer":"The Milky Way Galaxy"}
,
{"question":"Who was the first US President to declare war?","answer":"James Madison"}
,
{"question":"Who directed the movie \"Harry Potter and the Prisoner of Azkaban\"?","answer":"Alfonso Cuarón"}
,
{"question":"In science, how long is an eon?","answer":"A billion years"}
,
{"question":"Who was the first person to climb Mount Everest?","answer":"Sir Edmund Hillary"}
,
{"question":"Diamonds are made up almost entirely of what element?","answer":"Carbon"}
,
{"question":"What is the largest organ of the human body?","answer":"Skin"}
,
{"question":"How many US Supreme Court justices are there?","answer":"9"}
,
{"question":"Which character in the anime Attack on Titan is referred to as \"Humanity's Strongest Soldier\"?","answer":"Levi \"Rivaille\" Ackerman"}
,
{"question":"What famous horse won the Triple Crown in 1973?","answer":"Secretariat"}
,
{"question":"In what city does SpongeBob SquarePants live?","answer":"Bikini Bottom"}
,
{"question":"Tiger Woods became a professional golfer in what year?","answer":"1996"}
,
{"question":"What is the chemical symbol for Helium?","answer":"He"}
,
{"question":"How do you say goodbye in Spanish?","answer":"Adiós"}
,
{"question":"What is a group of owls called?","answer":"A parliament."}
,
{"question":"What is the capital of Peru?","answer":"Lima"}
,
{"question":"How many hydrogen atoms are in one molecule of water?","answer":"Two"}
,
{"question":"Which US president was known as \"The Great Communicator\"?","answer":"Ronald Regan"}
,
{"question":"What is a traditional fermented Korean side dish made seasoned vegetables and salt?","answer":"Kimchi"}
,
{"question":"Catalonia is a region of what country?","answer":"Spain"}
,
{"question":"CERN launched the very first website in what year?","answer":"1990"}
,
{"question":"What was the name of Robert E. Lee's most famous horse?","answer":"Traveller"}
,
{"question":"Who played Dracula in the 1931 vampire-horror film \"Dracula\"?","answer":"Bela Lugosi"}
,
{"question":"In which US state would you find Stone Mountain Park?","answer":"Georgia"}
,
{"question":"A teetotaler is a person that never drinks what?","answer":"Alcohol"}
,
{"question":"Who was the first human to travel into space?","answer":"Yuri Gagarin"}
,
{"question":"A tandoor is a type of what?","answer":"Oven"}
,
{"question":"A puggle is a cross between which two dog breeds?","answer":"Pug and Beagle"}
,
{"question":"The Roman numeral \"D\" stands for what number?","answer":"500"}
,
{"question":"How do you say \"hello\" in German?","answer":"Hallo"}
,
{"question":"Malcolm Little was a civil rights activist better known by what name?","answer":"Malcolm X"}
,
{"question":"How many states are needed to ratify an amendment for it to become part of the constitution?","answer":"Three-fourths of the states (38 of 50)"}
,
{"question":"What is the name of Washington Iriving's 1819 short story about a man that fell asleep in the woods for 20 years?","answer":"Rip Van Winkle"}
,
{"question":"What is the name for the Greek goddess of victory?","answer":"Nike"}
,
{"question":"Who was the female lead in the movie \"Titanic\"?","answer":"Kate Winslet"}
,
{"question":"In what year did the Apollo 7 human spaceflight take place?","answer":"1968"}
,
{"question":"What day is Thanksgiving celebrated in Canada?","answer":"The second Monday of October"}
,
{"question":"Sodium chloride is most commonly called what?","answer":"Salt"}
,
{"question":"Which mammal has the longest gestation period?","answer":"Elephants"}
,
{"question":"Kinnikinnick is a Native American herbal mixture used as a substitute for what?","answer":"Tobacco"}
,
{"question":"The use of reflected sounds to locate objects is known as what?","answer":"Echolocation"}
,
{"question":"The Southern Ocean surrounds which continent?","answer":"Antarctica"}
,
{"question":"The Statue of Liberty was a gift to the United States from which country?","answer":"France"}
,
{"question":"Kopi luwak is a very expensive type of what?","answer":"Coffee"}
,
{"question":"Who wrote the 1936 novel \"Gone with the Wind\"?","answer":"Margaret Mitchell"}
,
{"question":"The Arabian camel, also called dromedary, has how many humps?","answer":"One"}
,
{"question":"In what month is the longest day in the Northern Hemisphere?","answer":"June"}
,
{"question":"In the world of video games, what does NES stand for?","answer":"Nintendo Entertainment System"}
,
{"question":"Robert James \"Bobby\" Fischer is a famous champion of what game?","answer":"Chess"}
,
{"question":"What is the world's largest active volcano?","answer":"Mauna Loa (Hawaii)"}
,
{"question":"What is the word for \"Hello\" in Spanish?","answer":"Hola"}
,
{"question":"Who is the current supreme leader of North Korea?","answer":"Kim Jong Un"}
,
{"question":"Which actor that once played James Bond previously competed in the Mr. Universe bodybuilding competition?","answer":"Sean Connery"}
,
{"question":"What is the fear of clowns called?","answer":"Coulrophobia"}
,
{"question":"Which team won the 2016 Super Bowl?","answer":"Denver Broncos"}
,
{"question":"Who played the fictional anti hero Deadpool in the 2016 movie?","answer":"Ryan Reynolds"}
,
{"question":"Guinness beer was first brewed in which country?","answer":"Ireland"}
,
{"question":"Who is the author of the book \"A Brief History of Time\"?","answer":"Stephen Hawking"}
,
{"question":"In most countries it is illegal to call sparkling wine by what name unless it was produced in certain region of France?","answer":"Champagne"}
,
{"question":"The duck billed platypus is native to what country?","answer":"Australia"}
,
{"question":"How many furlongs are in a mile?","answer":"8"}
,
{"question":"The Electoral College in the United States is made up of how many electors?","answer":"538"}
,
{"question":"What is the highest number of Michelin stars a restaurant can receive?","answer":"3"}
,
{"question":"Who was the first emperor of China?","answer":"Qin Shi Huang (born Ying Zheng)"}
,
{"question":"How many keys are on most baby grand pianos?","answer":"88"}
,
{"question":"Which actor played the main character in the 1990 film \"Edward Scissorhands\"?","answer":"Johnny Depp"}
,
{"question":"What does the acronym DNA stand for?","answer":"Deoxyribonucleic acid"}
,
{"question":"Gymnophobia is the fear of what?","answer":"Nudity"}
,
{"question":"A person able to use both hands with equal skill is called what?","answer":"Ambidextrous"}
,
{"question":"Superman is a fictional superhero from what fictional planet?","answer":"Krypton"}
,
{"question":"Canada is made up of how many provinces?","answer":"10"}
,
{"question":"Who was the lead singer of the band Audioslave?","answer":"Chris Cornell"}
,
{"question":"What do the letters in NCAA, the name of the association that regulates athletes, stand for?","answer":"National Collegiate Athletic Association"}
,
{"question":"Snoopy from the comic peanuts is what breed of dog?","answer":"Beagle"}
,
{"question":"Which artist is credited with developing linear perspective?","answer":"Brunelleschi"}
,
{"question":"What is the oldest city in the United States?","answer":"Saint Augustine, Florida"}
,
{"question":"Which political party promotes individual liberty, free markets, non-interventionism and limited government?","answer":"Libertarian"}
,
{"question":"Who directed the movie \"Reservoir Dogs\"?","answer":"Quentin Tarantino"}
,
{"question":"Which state of the United States is the smallest?","answer":"Rhode Island"}
,
{"question":"Who wrote the fairy tale \"The Ugly Duckling\"?","answer":"Hans Christian Andersen"}
,
{"question":"What natural phenomena are measured by the Richter scale?","answer":"Earthquakes"}
,
{"question":"What is the chemical formula for ozone?","answer":"O3"}
,
{"question":"Diana Prince is the public persona of which fictional superhero?","answer":"Wonder Woman"}
,
{"question":"Who was the lead singer for the rock and roll band \"The Crickets\"?","answer":"Buddy Holly"}
,
{"question":"Gumbo is a stew that originated in which state?","answer":"Louisiana"}
,
{"question":"The companies HP, Microsoft and Apple were all started in a what?","answer":"Garage"}
,
{"question":"Now extinct, what shark is thought to have been the largest ever on Earth?","answer":"Megalodon"}
,
{"question":"In the 1986 blockbuster \"Top Gun\" which actress played Goose's wife?","answer":"Meg Ryan"}
,
{"question":"According to Greek mythology which Gorgon had snakes for hair and could turn onlookers into stone?","answer":"Medusa"}
,
{"question":"The US military installation Area 51 is located in which state?","answer":"Nevada"}
,
{"question":"In What state was President Barack Obama born?","answer":"Hawaii"}
,
{"question":"Who was the oldest person to sign the Declaration of Independence?","answer":"Benjamin Franklin"}
,
{"question":"New Orleans is known as the birthplace of what type of music?","answer":"Jazz"}
,
{"question":"What French sculptor created the Statue of Liberty?","answer":"Frédéric Auguste Bartholdi"}
,
{"question":"The Great Gatsby was written by which author?","answer":"F. Scott Fitzgerald"}
,
{"question":"In what year was Queen Elizabeth II born?","answer":"1926"}
,
{"question":"An octopus can fit through any hole larger than its what?","answer":"Beak"}
,
{"question":"On the hit show Seinfeld what was Kramer's first name?","answer":"Cosmo"}
,
{"question":"Which pop star sang the national anthem at the 50th Super Bowl?","answer":"Lady Gaga"}
,
{"question":"Most adults have how many canine teeth?","answer":"Four"}
,
{"question":"Who played Batman in the 1989 Tim Burton version of the film?","answer":"Michael Keaton"}
,
{"question":"The meat of a game animal, such as deer, is called what?","answer":"Venison"}
,
{"question":"The Walker Law passed in 1920 in New York was a law regulating which sport?","answer":"Boxing"}
,
{"question":"How many acres are in a square mile?","answer":"640"}
,
{"question":"What is the name of the main protagonist in the Legend of Zelda series of video games?","answer":"Link"}
,
{"question":"What is the smallest planet in our solar system?","answer":"Mercury"}
,
{"question":"Who was the shortest player ever to play in the NBA?","answer":"Tyrone Bogues, better known as Muggsy Bogues"}
,
{"question":"In what year did the French revolution begin?","answer":"1789"}
,
{"question":"Which artist created the sculpture \"The Thinker\"?","answer":"Auguste Rodin"}
,
{"question":"Which shark is the biggest?","answer":"The whale shark"}
,
{"question":"Fonts that contain small decorative lines at the end of a stroke are known as what?","answer":"Serif Fonts"}
,
{"question":"What language do they speak in Brazil?","answer":"Portuguese"}
]

if __name__ == "__main__":
   print('in module')
