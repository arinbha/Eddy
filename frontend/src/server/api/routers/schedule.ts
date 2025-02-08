import { z } from "zod";

import {
    createTRPCRouter,
    protectedProcedure,
    publicProcedure,
} from "~/server/api/trpc";

export const scheduleRouter = createTRPCRouter({
    upload_ics: protectedProcedure
        .input(z.object({
            userId: z.number(),
            ics: z.string()
        }))
        .query(async ({ ctx , input }) => {
            await ctx.client.post(`/users/${input.userId}/schedule/ics`, input.ics);
        }),

});
